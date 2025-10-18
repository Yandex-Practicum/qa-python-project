import pytest
import allure
import time


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("TC-01: Переход по клику на 'Конструктор'")
    @allure.description("Тест проверяет навигацию между конструктором и лентой заказов")
    def test_constructor_navigation(self, main_page):
        with allure.step("Перейти в ленту заказов"):
            main_page.click_order_feed()
            assert "feed" in main_page.get_current_url()

        with allure.step("Вернуться в конструктор через навигацию"):
            main_page.click_constructor()
            assert main_page.is_constructor_active()
            assert main_page.is_main_page_loaded()

    @allure.title("TC-02: Переход по клику на 'Лента Заказов'")
    @allure.description("Тест проверяет переход из конструктора в ленту заказов")
    def test_order_feed_navigation(self, main_page):
        with allure.step("Кликнуть на 'Лента Заказов'"):
            main_page.click_order_feed()

        with allure.step("Проверить переход на страницу ленты заказов"):
            assert "feed" in main_page.get_current_url()
            assert main_page.is_order_feed_active()

    @allure.title("TC-03: Открытие модального окна с деталями ингредиента")
    @allure.description("Тест проверяет открытие модального окна при клике на ингредиент")
    def test_ingredient_modal_opening(self, main_page):
        with allure.step("Кликнуть на первый ингредиент"):
            main_page.click_ingredient(0)

        with allure.step("Проверить отображение модального окна"):
            assert main_page.is_ingredient_modal_visible()

    @allure.title("TC-04: Закрытие модального окна ингредиента")
    @allure.description("Тест проверяет закрытие модального окна кликом по крестику")
    def test_ingredient_modal_closing(self, main_page, order_modal):
        with allure.step("Открыть модальное окно ингредиента"):
            main_page.click_ingredient(0)
            assert main_page.is_ingredient_modal_visible()

        with allure.step("Закрыть модальное окно"):
            assert order_modal.close_modal()

        with allure.step("Проверить закрытие модального окна"):
            assert not main_page.is_ingredient_modal_visible()

    @allure.title("TC-05: Увеличение счетчика ингредиента при добавлении")
    @allure.description("Тест проверяет увеличение счетчика ингредиента при добавлении в заказ")
    def test_ingredient_counter_increase(self, main_page, authenticated_user):
        with allure.step("Получить начальное значение счетчика ингредиента"):
            initial_counter = main_page.get_ingredient_counter(0)

        with allure.step("Добавить ингредиент в конструктор"):
            main_page.add_ingredient_to_constructor(0)

        with allure.step("Проверить увеличение счетчика"):
            new_counter = main_page.get_ingredient_counter(0)
            assert new_counter != initial_counter, "Счетчик ингредиента должен увеличиться"

    @allure.title("TC-06: Навигация по разделам конструктора")
    @allure.description("Тест проверяет переключение между разделами конструктора")
    def test_constructor_sections_navigation(self, main_page):
        with allure.step("Проверить активность раздела 'Булки' по умолчанию"):
            assert main_page.is_buns_section_active()

        with allure.step("Переключиться на раздел 'Соусы'"):
            main_page.click_sauces_section()
            assert main_page.is_sauces_section_active()

        with allure.step("Переключиться на раздел 'Начинки'"):
            main_page.click_fillings_section()
            assert main_page.is_fillings_section_active()

        with allure.step("Вернуться в раздел 'Булки'"):
            main_page.click_buns_section()
            assert main_page.is_buns_section_active()
