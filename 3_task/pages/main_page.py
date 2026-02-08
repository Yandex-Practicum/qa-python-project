import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):

    CONSTRUCTOR_TAB = (By.XPATH, "//p[text()='Конструктор']")
    FEED_TAB = (By.XPATH, "//a[contains(@href,'/feed')]")

    CONSTRUCTOR_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    FEED_HEADER = (By.XPATH, "//h1[text()='Лента заказов']")

    INGREDIENT_NAME = "Соус Spicy-X"
    INGREDIENT = (By.XPATH, f"//p[text()='{INGREDIENT_NAME}']")

    CONSTRUCTOR_SECTION = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor')]"
    )

    CONSTRUCTOR_ITEMS = (
        By.XPATH,
        "//section[contains(@class,'BurgerConstructor')]//li"
    )

    MODAL = (By.XPATH, "//section[contains(@class,'Modal_modal')]")
    MODAL_CLOSE_BUTTON = (
        By.XPATH,
        "//button[contains(@class,'Modal_modal__close')]"
    )

    # ---------- навигация ----------

    @allure.step("Открыть конструктор")
    def open_constructor(self):
        self.click(self.CONSTRUCTOR_TAB)

    @allure.step("Открыть ленту заказов")
    def open_feed(self):
        self.click(self.FEED_TAB)

    # ---------- проверки ----------

    @allure.step("Проверить, что конструктор открыт")
    def is_constructor_opened(self) -> bool:
        return self.count_elements(self.CONSTRUCTOR_HEADER) > 0

    @allure.step("Проверить, что лента заказов открыта")
    def is_feed_opened(self) -> bool:
        return self.count_elements(self.FEED_HEADER) > 0

    # ---------- модалка ----------

    @allure.step("Открыть модальное окно ингредиента")
    def open_ingredient_modal(self):
        self.click(self.INGREDIENT)
        self.wait_visible(self.MODAL)

    @allure.step("Закрыть модальное окно ингредиента")
    def close_ingredient_modal(self):
        self.click(self.MODAL_CLOSE_BUTTON)

    @allure.step("Дождаться закрытия модального окна")
    def wait_modal_closed(self):
        self.wait_invisible(self.MODAL)

    # ---------- конструктор ----------

    @allure.step("Добавить ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        ingredient = self.wait_present(self.INGREDIENT)
        target = self.wait_present(self.CONSTRUCTOR_SECTION)

        self.execute_js(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', { dataTransfer }));
            target.dispatchEvent(new DragEvent('dragover', { dataTransfer }));
            target.dispatchEvent(new DragEvent('drop', { dataTransfer }));
            source.dispatchEvent(new DragEvent('dragend', { dataTransfer }));
            """,
            ingredient,
            target
        )

    @allure.step("Проверить, что в конструкторе есть ингредиенты")
    def constructor_has_items(self) -> bool:
        return self.count_elements(self.CONSTRUCTOR_ITEMS) > 0
