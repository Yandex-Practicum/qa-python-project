import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome",
                     help="browser to run tests: chrome or firefox")
    parser.addoption("--headless", action="store_true", help="run tests in headless mode")


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
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_experimental_option("excludeSwitches", ["enable-automation"])

            driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif browser_name == "firefox":
            options = FirefoxOptions()
            if headless:
                options.add_argument("--headless")
            options.set_preference("dom.webdriver.enabled", False)
            options.set_preference("useAutomationExtension", False)

            driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

        driver.implicitly_wait(10)
        driver.set_page_load_timeout(30)
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
def main_page(browser):
    from pages.main_page import MainPage
    page = MainPage(browser)
    page.open()
    page.wait_for_main_page_loaded()
    return page


@pytest.fixture
def order_feed_page(browser):
    from pages.order_feed_page import OrderFeedPage
    page = OrderFeedPage(browser)
    page.open()
    page.wait_for_page_loaded()
    return page


@pytest.fixture
def login_page(browser):
    from pages.login_page import LoginPage
    page = LoginPage(browser)
    page.open()
    return page


@pytest.fixture
def authorized_user(main_page, login_page):
    """Фикстура для авторизованного пользователя"""
    from helpers.data_helper import DataHelper

    test_email = DataHelper.get_test_user_email()
    test_password = DataHelper.get_test_user_password()

    main_page.click_personal_account()
    login_page.complete_login(test_email, test_password)
    main_page.wait_for_main_page_loaded()

    return main_page


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
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
