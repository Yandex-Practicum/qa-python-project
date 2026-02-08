import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver, timeout=10):
        self._driver = driver
        self._wait = WebDriverWait(driver, timeout)

    # ---------- базовые ожидания ----------

    @allure.step("Ожидание видимости элемента {locator}")
    def wait_visible(self, locator):
        return self._wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Ожидание кликабельности элемента {locator}")
    def wait_clickable(self, locator):
        return self._wait.until(EC.element_to_be_clickable(locator))

    @allure.step("Ожидание присутствия элемента {locator}")
    def wait_present(self, locator):
        return self._wait.until(EC.presence_of_element_located(locator))

    @allure.step("Ожидание исчезновения элемента {locator}")
    def wait_invisible(self, locator):
        self._wait.until(EC.invisibility_of_element_located(locator))

    # ---------- действия ----------

    @allure.step("Клик по элементу {locator}")
    def click(self, locator):
        element = self.wait_clickable(locator)
        self._driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        self._driver.execute_script("arguments[0].click();", element)

    @allure.step("Выполнение JS-скрипта")
    def execute_js(self, script, *args):
        self._driver.execute_script(script, *args)

    @allure.step("Обновление страницы")
    def refresh_page(self):
        self._driver.refresh()

    # ---------- получение данных ----------

    @allure.step("Получение текста элемента {locator}")
    def get_text(self, locator) -> str:
        return self.wait_visible(locator).text

    @allure.step("Подсчёт элементов {locator}")
    def count_elements(self, locator) -> int:
        return len(self._driver.find_elements(*locator))

    @allure.step("Проверка видимости элемента {locator}")
    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except Exception:
            return False
