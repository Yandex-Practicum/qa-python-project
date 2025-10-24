import allure
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from locators.order_modal_locators import OrderModalLocators


class OrderModal(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Проверить видимость модального окна")
    def is_modal_visible(self):
        return self.is_visible(OrderModalLocators.MODAL)

    @allure.step("Закрыть модальное окно")
    def close_modal(self):
        return self._close_by_close_button()

    def _close_by_close_button(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_CLOSE):
                self.click(OrderModalLocators.MODAL_CLOSE)
                return True
        except:
            pass
        return False

    @allure.step("Получить номер заказа из модального окна")
    def get_order_number(self):
        try:
            order_number_element = self.find_element(OrderModalLocators.ORDER_NUMBER, timeout=10)
            return order_number_element.text
        except:
            return None

    @allure.step("Получить название ингредиента из модального окна")
    def get_ingredient_name(self):
        try:
            ingredient_name_element = self.find_element(OrderModalLocators.INGREDIENT_NAME, timeout=10)
            return ingredient_name_element.text
        except:
            return None
