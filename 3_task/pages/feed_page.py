import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FeedPage(BasePage):

    ORDERS_TOTAL = (
        By.XPATH,
        "//p[text()='Выполнено за все время:']/following-sibling::p"
    )
    ORDERS_TODAY = (
        By.XPATH,
        "//p[text()='Выполнено за сегодня:']/following-sibling::p"
    )
    ORDERS_IN_PROGRESS = (
        By.XPATH,
        "//ul[contains(@class,'OrderFeed_orderList')]"
    )

    @allure.step("Получение количества заказов за всё время")
    def get_total_orders(self) -> int:
        return int(self.get_text(self.ORDERS_TOTAL))

    @allure.step("Получение количества заказов за сегодня")
    def get_today_orders(self) -> int:
        return int(self.get_text(self.ORDERS_TODAY))

    @allure.step("Обновление страницы ленты заказов")
    def refresh_feed(self):
        self.refresh_page()

    @allure.step("Проверка наличия заказов в статусе «В работе»")
    def has_orders_in_progress(self) -> bool:
        return self.is_visible(self.ORDERS_IN_PROGRESS)
