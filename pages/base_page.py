import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from helpers.wait_helper import WaitHelper
from helpers.url_helper import UrlHelper


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WaitHelper(driver)
        self.url_helper = UrlHelper()

    @allure.step("Открыть URL: {url}")
    def open_url(self, url):
        self.driver.get(url)
        self.wait.wait_for_page_load()
        return self

    @allure.step("Открыть страницу: {page_name}")
    def open_page(self, page_name):
        url = self.url_helper.get_url(page_name)
        return self.open_url(url)

    @allure.step("Найти элемент: {locator}")
    def find_element(self, locator, timeout=10):
        return self.wait.wait_for_element_present(locator, timeout)

    @allure.step("Найти элементы: {locator}")
    def find_elements(self, locator, timeout=10):
        return self.wait.wait_for_elements_present(locator, timeout)

    @allure.step("Кликнуть на элемент: {locator}")
    def click(self, locator, timeout=10):
        element = self.wait.wait_for_element_clickable(locator, timeout)
        element.click()
        return self

    @allure.step("Ввести текст: '{text}' в элемент: {locator}")
    def type_text(self, locator, text, timeout=10):
        element = self.wait.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)
        return self

    @allure.step("Получить текст элемента: {locator}")
    def get_text(self, locator, timeout=10):
        element = self.wait.wait_for_element_visible(locator, timeout)
        return element.text

    @allure.step("Проверить видимость элемента: {locator}")
    def is_visible(self, locator, timeout=5):
        try:
            self.wait.wait_for_element_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверить наличие элемента: {locator}")
    def is_present(self, locator, timeout=5):
        try:
            self.wait.wait_for_element_present(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Получить текущий URL")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Выполнить JavaScript: {script}")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Сделать скриншот")
    def take_screenshot(self, name="screenshot"):
        allure.attach(
            self.driver.get_screenshot_as_png(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
