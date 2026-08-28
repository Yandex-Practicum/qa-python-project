import allure
import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage


@pytest.mark.ui
@allure.epic("Stellar Burgers")
@allure.feature("Основная функциональность")
class TestMainFunctionality:
    @allure.title("Переход в Конструктор по клику")
    def test_constructor_link_opens_constructor(self, driver):
        page = LoginPage(driver)
        page.open("/login")
        page.wait_loaded()

        page.click_constructor()

        MainPage(driver).wait_loaded()
        assert driver.current_url.endswith("/")

    @allure.title("Переход в Ленту заказов по клику")
    def test_order_feed_link_opens_feed(self, driver):
        page = MainPage(driver)
        page.open("/")
        page.wait_loaded()

        page.click_order_feed()

        assert driver.current_url.endswith("/feed")

    @allure.title("Клик по ингредиенту открывает окно с деталями")
    def test_ingredient_click_opens_details_modal(self, driver):
        page = MainPage(driver)
        page.open("/")
        page.wait_loaded()

        page.open_first_ingredient()

        assert page.ingredient_modal_is_open()

    @allure.title("Крестик закрывает окно с деталями ингредиента")
    def test_close_button_closes_ingredient_modal(self, driver):
        page = MainPage(driver)
        page.open("/")
        page.wait_loaded()
        page.open_first_ingredient()

        page.close_ingredient_modal()

        assert page.ingredient_modal_is_closed()

    @allure.title("После добавления ингредиента его счётчик увеличивается")
    def test_ingredient_counter_increases_after_dragging(self, driver):
        page = MainPage(driver)
        page.open("/")
        page.wait_loaded()
        counter_before = page.get_first_filling_counter()

        counter_after = page.add_first_filling()

        assert counter_after > counter_before
