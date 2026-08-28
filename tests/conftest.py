import allure
import os
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from api_client import StellarBurgersApi
from data import generate_user_data


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Браузер для UI-тестов: chrome или firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запустить браузер без графического окна",
    )


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    allure.dynamic.parameter("browser", browser_name)

    # Selenium Manager сам выбирает драйвер, совместимый с установленным
    # браузером. Исключаем из поиска старые драйверы из пользовательского PATH.
    original_path = os.environ.get("PATH", "")
    os.environ["PATH"] = os.pathsep.join(
        path
        for path in original_path.split(os.pathsep)
        if "webdriver" not in path.lower()
    )

    try:
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless=new")
            options.add_argument("--window-size=1440,1000")
            browser = webdriver.Chrome(options=options)
        else:
            options = FirefoxOptions()
            if headless:
                options.add_argument("-headless")
            browser = webdriver.Firefox(options=options)
            browser.set_window_size(1440, 1000)
    finally:
        os.environ["PATH"] = original_path

    browser.set_page_load_timeout(40)
    yield browser

    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        allure.attach(
            browser.get_screenshot_as_png(),
            name=f"Ошибка_{browser_name}",
            attachment_type=allure.attachment_type.PNG,
        )
    browser.quit()


@pytest.fixture(scope="session")
def ui_user():
    client = StellarBurgersApi()
    payload = generate_user_data()
    access_token = None
    last_error = None

    for _ in range(3):
        try:
            response = client.create_user(payload)
            if response.status_code == 200:
                access_token = response.json()["accessToken"]
                break

            # После сетевого таймаута пользователь мог успеть создаться.
            # В этом случае повторная регистрация вернёт 403, а логин — токен.
            if response.status_code == 403:
                login_response = client.login_user(payload)
                if login_response.status_code == 200:
                    access_token = login_response.json()["accessToken"]
                    break
            response.raise_for_status()
        except requests.RequestException as error:
            last_error = error
            try:
                login_response = client.login_user(payload)
                if login_response.status_code == 200:
                    access_token = login_response.json()["accessToken"]
                    break
            except requests.RequestException as login_error:
                last_error = login_error

    if access_token is None:
        client.close()
        if last_error is not None:
            raise last_error
        pytest.fail("Не удалось создать пользователя для UI-тестов")

    yield payload

    try:
        client.delete_user(access_token)
    except requests.RequestException:
        pass
    finally:
        client.close()
