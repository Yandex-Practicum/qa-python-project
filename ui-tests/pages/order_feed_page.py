import allure
import time
from pages.base_page import BasePage
from locators.order_feed_locators import OrderFeedLocators


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderFeedLocators()

    @allure.step("Открыть страницу ленты заказов")
    def open(self):
        return self.open_page("feed")

    @allure.step("Дождаться загрузки ленты заказов")
    def wait_for_page_loaded(self):
        self.wait.wait_for_page_load()
        assert self.is_visible(self.locators.ORDER_FEED_SECTION), "Лента заказов не загрузилась"
        return True

    @allure.step("Получить количество выполненных заказов за все время")
    def get_total_orders_count(self):
        try:
            total_orders = self.find_element(self.locators.TOTAL_ORDERS)
            return int(total_orders.text.replace(' ', ''))
        except:
            return 0

    @allure.step("Получить количество выполненных заказов за сегодня")
    def get_today_orders_count(self):
        try:
            today_orders = self.find_element(self.locators.TODAY_ORDERS)
            return int(today_orders.text.replace(' ', ''))
        except:
            return 0

    @allure.step("Получить номера заказов в работе")
    def get_orders_in_progress(self):
        if self.is_visible(self.locators.IN_PROGRESS_SECTION):
            order_elements = self.find_elements(self.locators.ORDERS_IN_PROGRESS)
            return [order.text for order in order_elements]
        return []

    @allure.step("Проверить наличие заказа в разделе 'В работе'")
    def is_order_in_progress(self, order_number):
        orders_in_progress = self.get_orders_in_progress()
        return order_number in orders_in_progress

    @allure.step("Получить список всех отображаемых заказов")
    def get_all_visible_orders(self):
        try:
            order_elements = self.find_elements(self.locators.ORDER_ITEMS)
            orders_data = []
            for order in order_elements:
                try:
                    number_element = order.find_element(*self.locators.ORDER_NUMBER)
                    orders_data.append(number_element.text)
                except:
                    continue
            return orders_data
        except:
            return []
