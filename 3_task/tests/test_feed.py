import allure

from pages.feed_page import FeedPage
from pages.main_page import MainPage


@allure.feature("Лента заказов")
class TestFeed:

    @allure.title("Отображение и обновление счётчиков заказов в ленте")
    def test_orders_counters_display_and_update(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("Переход в конструктор"):
            main_page.open_constructor()

        with allure.step("Добавление ингредиента в конструктор"):
            main_page.add_ingredient_to_constructor()
            assert main_page.constructor_has_items()

        with allure.step("Переход в ленту заказов"):
            main_page.open_feed()

        with allure.step("Фиксация текущих значений счётчиков"):
            total_before = feed_page.get_total_orders()

        with allure.step("Обновление ленты заказов"):
            feed_page.refresh_feed()

        with allure.step("Проверка, что счётчик выполненных заказов не уменьшился"):
            assert feed_page.get_total_orders() >= total_before

    @allure.title("В ленте заказов отображается раздел «В работе»")
    def test_orders_in_progress_section_displayed(self, driver):
        main_page = MainPage(driver)
        feed_page = FeedPage(driver)

        with allure.step("Переход в конструктор"):
            main_page.open_constructor()

        with allure.step("Добавление ингредиента в конструктор"):
            main_page.add_ingredient_to_constructor()
            assert main_page.constructor_has_items()

        with allure.step("Переход в ленту заказов"):
            main_page.open_feed()

        with allure.step("Обновление ленты заказов"):
            feed_page.refresh_feed()

        with allure.step("Проверка наличия раздела «В работе»"):
            assert feed_page.has_orders_in_progress()
