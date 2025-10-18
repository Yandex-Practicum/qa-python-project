import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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
        methods = [
            self._close_by_close_button,
            self._close_by_escape,
            self._close_by_overlay_click
        ]

        for method in methods:
            try:
                if method():
                    return True
            except:
                continue

        return False

    def _close_by_close_button(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_CLOSE):
                self.click(OrderModalLocators.MODAL_CLOSE)
                return True
        except:
            pass
        return False

    def _close_by_escape(self):
        try:
            actions = ActionChains(self.driver)
            actions.send_keys(Keys.ESCAPE).perform()
            return True
        except:
            return False

    def _close_by_overlay_click(self):
        try:
            if self.is_visible(OrderModalLocators.MODAL_OVERLAY):
                self.click(OrderModalLocators.MODAL_OVERLAY)
                return True
        except:
            pass
        return False
