import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


class WaitHelper:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, timeout)

    @allure.step("Дождаться присутствия элемента: {locator}")
    def wait_for_element_present(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.presence_of_element_located(locator))

    @allure.step("Дождаться видимости элемента: {locator}")
    def wait_for_element_visible(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Дождаться кликабельности элемента: {locator}")
    def wait_for_element_clickable(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Дождаться скрытия элемента: {locator}")
    def wait_for_element_not_visible(self, locator, timeout=None):
        wait_timeout = timeout or self.timeout
        wait = WebDriverWait(self.driver, wait_timeout)
        return wait.until(EC.invisibility_of_element_located(locator))

    @allure.step("Дождаться загрузки страницы")
    def wait_for_page_load(self, timeout=30):
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
        except TimeoutException:
            raise Exception(f"Page not loaded within {timeout} seconds")
