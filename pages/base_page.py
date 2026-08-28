import allure
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    TimeoutException,
)
from selenium.webdriver.support import expected_conditions as conditions
from selenium.webdriver.support.ui import WebDriverWait

from constants import BASE_URL
from locators import HeaderLocators


class BasePage:
    WAIT_TIMEOUT = 25

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.WAIT_TIMEOUT)

    @allure.step("Открыть страницу {path}")
    def open(self, path="/"):
        url = f"{BASE_URL}{path}"
        for attempt in range(2):
            try:
                self.driver.get(url)
                return
            except TimeoutException:
                self.driver.execute_script("window.stop();")
                if attempt == 1:
                    raise

    def find_visible(self, locator):
        return self.wait.until(conditions.visibility_of_element_located(locator))

    def find_clickable(self, locator):
        return self.wait.until(conditions.element_to_be_clickable(locator))

    def find_all(self, locator):
        return self.wait.until(conditions.presence_of_all_elements_located(locator))

    def wait_page_loaded(self, locator, path):
        """Дождаться ключевого элемента страницы, при сбое перезагрузить её."""
        for attempt in range(3):
            try:
                return self.find_visible(locator)
            except TimeoutException:
                if attempt == 2:
                    raise
                self.open(path)

    def click(self, locator):
        element = self.find_clickable(locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click();", element)

    def get_text(self, locator):
        return self.find_visible(locator).text

    def wait_url(self, path):
        expected_url = f"{BASE_URL}{path}"
        self.wait.until(conditions.url_to_be(expected_url))

    def wait_invisible(self, locator):
        self.wait.until(conditions.invisibility_of_element_located(locator))

    @allure.step("Перейти в Конструктор")
    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR_LINK)
        self.wait_url("/")

    @allure.step("Перейти в Ленту заказов")
    def click_order_feed(self):
        self.click(HeaderLocators.ORDER_FEED_LINK)
        self.wait_url("/feed")
