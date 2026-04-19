from pages.base_page import BasePage
from data.locators import FeedPageLocators
import logging

class FeedPage(BasePage):

    def open_feed(self):
        self.driver.get("https://stellarburgers.education-services.ru/feed")

    def get_total_done(self):
        return int(self.get_text(FeedPageLocators.TOTAL_DONE))

    def get_today_done(self):
        return int(self.get_text(FeedPageLocators.TODAY_DONE))

    def order_exists(self, number):
        formatted_number = f"{int(number):07d}"
        def check(_):
            orders = self.find_elements(FeedPageLocators.ORDER_ITEMS)
            return any(
                formatted_number == order.text.strip()
                for order in orders
            )
        return self.wait.until(check)