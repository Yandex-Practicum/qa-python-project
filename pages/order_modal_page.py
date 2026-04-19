from pages.base_page import BasePage
from data.locators import OrderModalLocators


class OrderModalPage(BasePage):

    def get_order_number(self):

        # 1. берём текущее значение (до обновления)
        old_number = self.get_text(OrderModalLocators.ORDER_NUMBER)

        # 2. ждём, пока оно изменится
        self.wait.until(
            lambda d: self.get_text(OrderModalLocators.ORDER_NUMBER) != old_number
        )

        # 3. берём финальное значение
        text = self.get_text(OrderModalLocators.ORDER_NUMBER)
        number = "".join(filter(str.isdigit, text))

        assert number != "", "Order number is empty"

        return number