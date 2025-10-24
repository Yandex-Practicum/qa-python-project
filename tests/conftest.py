import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from helpers.data_helper import DataHelper


# Глобальная переменная для отслеживания добавленных опций
_OPTIONS_ADDED = False


def pytest_addoption(parser):
    """Добавляем кастомные опции только один раз"""
    global _OPTIONS_ADDED

    if _OPTIONS_ADDED:
        return

    parser.addoption("--browser", action="store", default="chrome",
                    help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true",
                    help="run tests in headless mode")

    _OPTIONS_ADDED = True


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")

    driver = None

    try:
        if browser_name == "chrome":
            options = ChromeOptions()
            if headless:
                options.add_argument("--headless")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-gpu")
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            # Используем webdriver-manager с последней версией
            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser_name == "firefox":
            # Временно отключаем Firefox из-за проблем с совместимостью
            pytest.skip("Firefox временно отключен из-за проблем с драйверами")
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.implicitly_wait(10)
        driver.maximize_window()

        yield driver

    except Exception as e:
        pytest.fail(f"Browser setup failed: {str(e)}")

    finally:
        if driver:
            try:
                driver.quit()
            except Exception:
                pass


@pytest.fixture
def authenticated_user(browser):
    """Фикстура для авторизованного пользователя"""
    from pages.main_page import MainPage
    from pages.login_page import LoginPage
    
    # Создаем экземпляры страниц
    main_page = MainPage(browser)
    login_page = LoginPage(browser)
    
    # Используем тестовые данные из DataHelper
    test_email = DataHelper.get_test_user_email()
    test_password = DataHelper.get_test_user_password()

    # Открываем главную страницу
    main_page.open()
    main_page.wait_for_main_page_loaded()

    # Переходим на страницу логина
    main_page.click_personal_account()

    # Выполняем логин
    login_page.enter_email(test_email)
    login_page.enter_password(test_password)
    login_page.click_login_button()

    # Ждем загрузки главной страницы после логина
    main_page.wait_for_main_page_loaded()

    return main_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Хук для создания скриншотов при падении тестов"""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        try:
            browser = item.funcargs.get('browser')
            if browser:
                allure.attach(
                    browser.get_screenshot_as_png(),
                    name="screenshot_on_failure",
                    attachment_type=allure.attachment_type.PNG
                )
        except Exception:
            pass
