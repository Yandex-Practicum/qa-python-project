from pages.base_page import BasePage
from data.locators import ModalLocators


class ModalPage(BasePage):

    def is_open(self):
        try:
            return self.wait_visible(ModalLocators.MODAL).is_displayed()
        except:
            return False

    def close(self):
        self.click(ModalLocators.CLOSE)

    def wait_closed(self):
        return self.wait_invisible(ModalLocators.MODAL)