import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import ActionChains

from locators import IngredientModalLocators, MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    def wait_loaded(self):
        self.wait_page_loaded(MainPageLocators.PAGE_TITLE, "/")

    @allure.step("Открыть детали первого ингредиента")
    def open_first_ingredient(self):
        self.click(MainPageLocators.FIRST_BUN)
        self.find_visible(IngredientModalLocators.MODAL)

    def ingredient_modal_is_open(self):
        return self.find_visible(IngredientModalLocators.TITLE).is_displayed()

    @allure.step("Закрыть окно с деталями ингредиента")
    def close_ingredient_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)
        self.wait_invisible(IngredientModalLocators.OVERLAY)

    def ingredient_modal_is_closed(self):
        elements = self.driver.find_elements(*IngredientModalLocators.TITLE)
        return not any(element.is_displayed() for element in elements)

    def get_first_filling_counter(self):
        return int(self.get_text(MainPageLocators.FIRST_FILLING_COUNTER))

    def _html5_drag_and_drop(self, source, target):
        script = """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();
            source.dispatchEvent(new DragEvent('dragstart', {
                bubbles: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragenter', {
                bubbles: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('dragover', {
                bubbles: true, dataTransfer: dataTransfer
            }));
            target.dispatchEvent(new DragEvent('drop', {
                bubbles: true, dataTransfer: dataTransfer
            }));
            source.dispatchEvent(new DragEvent('dragend', {
                bubbles: true, dataTransfer: dataTransfer
            }));
        """
        self.driver.execute_script(script, source, target)

    def _drag_ingredient(self, ingredient_locator):
        source = self.find_visible(ingredient_locator)
        target = self.find_visible(MainPageLocators.CONSTRUCTOR_BASKET)
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", source
        )
        ActionChains(self.driver).click_and_hold(source).pause(0.3).move_to_element(
            target
        ).pause(0.5).release().perform()

    @allure.step("Добавить начинку в конструктор")
    def add_first_filling(self):
        counter_before = self.get_first_filling_counter()
        self._drag_ingredient(MainPageLocators.FIRST_FILLING)
        try:
            self.wait.until(
                lambda _: self.get_first_filling_counter() > counter_before
            )
        except TimeoutException:
            source = self.find_visible(MainPageLocators.FIRST_FILLING)
            target = self.find_visible(MainPageLocators.CONSTRUCTOR_BASKET)
            self._html5_drag_and_drop(source, target)
            self.wait.until(
                lambda _: self.get_first_filling_counter() > counter_before
            )
        return self.get_first_filling_counter()

    @allure.step("Добавить булку в конструктор")
    def add_first_bun(self):
        self._drag_ingredient(MainPageLocators.FIRST_BUN)

    @allure.step("Оформить заказ и получить его номер")
    def submit_order(self):
        self.click(MainPageLocators.ORDER_BUTTON)

        def order_number_is_ready(driver):
            text = driver.find_element(*MainPageLocators.ORDER_NUMBER).text.strip()
            return text if text.isdigit() and text != "9999" else False

        return int(self.wait.until(order_number_is_ready))

    @allure.step("Закрыть окно оформленного заказа")
    def close_order_modal(self):
        self.click(IngredientModalLocators.CLOSE_BUTTON)
        self.wait_invisible(IngredientModalLocators.OVERLAY)

    def create_order(self):
        self.add_first_bun()
        self.add_first_filling()
        return self.submit_order()
