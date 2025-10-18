import pytest
import allure


@allure.feature("Дополнительные сценарии")
class TestAdditionalScenarios:

    @allure.title("TC-13: Проверка авторизации перед созданием заказа")
    @allure.description("Тест проверяет, что неавторизованный пользователь перенаправляется на страницу логина")
    def test_redirect_to_login_for_unauthorized_user(self, main_page, login_page):
        with allure.step("Попытаться создать заказ без авторизации"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.click_make_order()

        with allure.step("Проверить перенаправление на страницу логина"):
            assert login_page.is_login_form_present()
            assert "login" in login_page.get_current_url()

    @allure.title("TC-14: Работа модального окна с деталями ингредиента")
    @allure.description("Тест проверяет корректность отображения информации в модальном окне ингредиента")
    def test_ingredient_modal_content(self, main_page, order_modal):
        with allure.step("Открыть модальное окно ингредиента"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.click_ingredient(0)

        with allure.step("Проверить содержимое модального окна"):
            assert order_modal.is_modal_visible()
            ingredient_name = order_modal.get_ingredient_name()
            assert ingredient_name is not None and ingredient_name != "", "Название ингредиента должно отображаться"

        with allure.step("Закрыть модальное окно и проверить возврат на главную"):
            order_modal.close_modal()
            assert main_page.is_main_page_loaded()

    @allure.title("TC-15: Взаимодействие с конструктором бургеров")
    @allure.description("Тест проверяет базовое взаимодействие с конструктором")
    def test_burger_constructor_interaction(self, main_page, authenticated_user):
        with allure.step("Добавить несколько ингредиентов в конструктор"):
            main_page.open()
            main_page.wait_for_main_page_loaded()

            # Добавляем разные типы ингредиентов
            main_page.add_ingredient_to_constructor(0)  # Булка
            main_page.add_ingredient_to_constructor(5)  # Соус
            main_page.add_ingredient_to_constructor(10) # Начинка

        with allure.step("Проверить возможность оформления заказа"):
            assert main_page.is_visible(main_page.locators.ORDER_BUTTON), "Кнопка оформления заказа должна быть доступна"

    @allure.title("TC-16: Проверка отзывчивости интерфейса")
    @allure.description("Тест проверяет производительность и отзывчивость пользовательского интерфейса")
    def test_ui_responsiveness(self, main_page):
        import time

        with allure.step("Измерить время загрузки главной страницы"):
            start_time = time.time()
            main_page.open()
            main_page.wait_for_main_page_loaded()
            load_time = time.time() - start_time

            assert load_time < 10, f"Страница должна загружаться быстрее 10 секунд. Фактическое время: {load_time:.2f}с"

        with allure.step("Измерить время открытия модального окна"):
            start_time = time.time()
            main_page.click_ingredient(0)
            modal_time = time.time() - start_time

            assert modal_time < 3, f"Модальное окно должно открываться быстрее 3 секунд. Фактическое время: {modal_time:.2f}с"
