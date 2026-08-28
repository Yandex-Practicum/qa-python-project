import allure
import pytest

from pages.feed_page import FeedPage
from pages.login_page import LoginPage
from pages.main_page import MainPage


def login_test_user(driver, ui_user):
    login_page = LoginPage(driver)
    login_page.open("/login")
    login_page.login(ui_user["email"], ui_user["password"])


@pytest.mark.ui
@allure.epic("Stellar Burgers")
@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("Новый заказ увеличивает счётчик за всё время")
    def test_new_order_increases_total_all_counter(self, driver, ui_user):
        login_test_user(driver, ui_user)
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = FeedPage(driver)
        feed_page.wait_loaded()
        counter_before = feed_page.get_total_all()

        feed_page.click_constructor()
        order_number = main_page.create_order()
        main_page.close_order_modal()
        main_page.click_order_feed()
        feed_page.wait_loaded()

        assert order_number > 0
        assert feed_page.wait_total_all_increased(counter_before)

    @allure.title("Новый заказ увеличивает счётчик за сегодня")
    def test_new_order_increases_total_today_counter(self, driver, ui_user):
        login_test_user(driver, ui_user)
        main_page = MainPage(driver)
        main_page.click_order_feed()
        feed_page = FeedPage(driver)
        feed_page.wait_loaded()
        counter_before = feed_page.get_total_today()

        feed_page.click_constructor()
        order_number = main_page.create_order()
        main_page.close_order_modal()
        main_page.click_order_feed()
        feed_page.wait_loaded()

        assert order_number > 0
        assert feed_page.wait_total_today_increased(counter_before)

    @allure.title("Номер нового заказа появляется в разделе В работе")
    def test_new_order_number_appears_in_progress(self, driver, ui_user):
        login_test_user(driver, ui_user)
        main_page = MainPage(driver)
        order_number = main_page.create_order()
        main_page.close_order_modal()
        main_page.click_order_feed()
        feed_page = FeedPage(driver)
        feed_page.wait_loaded()

        assert feed_page.wait_order_in_progress(order_number)
