import allure
from selenium.common.exceptions import TimeoutException

from locators import FeedPageLocators
from pages.base_page import BasePage


class FeedPage(BasePage):
    def wait_loaded(self):
        def feed_data_is_ready(driver):
            title = driver.find_elements(*FeedPageLocators.PAGE_TITLE)
            total_all = driver.find_elements(*FeedPageLocators.TOTAL_ALL)
            total_today = driver.find_elements(*FeedPageLocators.TOTAL_TODAY)
            return (
                title
                and title[0].is_displayed()
                and total_all
                and total_all[0].text.strip().isdigit()
                and total_today
                and total_today[0].text.strip().isdigit()
            )

        for attempt in range(3):
            try:
                self.wait.until(feed_data_is_ready)
                return
            except TimeoutException:
                if attempt == 2:
                    raise
                self.open("/feed")

    def get_total_all(self):
        return int(self.get_text(FeedPageLocators.TOTAL_ALL))

    def get_total_today(self):
        return int(self.get_text(FeedPageLocators.TOTAL_TODAY))

    @allure.step("Дождаться увеличения счётчика за всё время")
    def wait_total_all_increased(self, previous_value):
        return self.wait.until(
            lambda driver: int(
                driver.find_element(*FeedPageLocators.TOTAL_ALL).text
            )
            > previous_value
        )

    @allure.step("Дождаться увеличения счётчика за сегодня")
    def wait_total_today_increased(self, previous_value):
        return self.wait.until(
            lambda driver: int(
                driver.find_element(*FeedPageLocators.TOTAL_TODAY).text
            )
            > previous_value
        )

    @allure.step("Дождаться номера заказа в разделе В работе")
    def wait_order_in_progress(self, order_number):
        expected_number = f"0{order_number}"

        def order_appeared(driver):
            elements = driver.find_elements(*FeedPageLocators.IN_PROGRESS_ORDERS)
            return expected_number in [element.text.strip() for element in elements]

        return self.wait.until(order_appeared)
