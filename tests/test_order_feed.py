import pytest
import allure


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("TC-07: Увеличение счетчика 'Выполнено за всё время' при новом заказе")
    @allure.description("Тест проверяет увеличение общего счетчика заказов после создания нового заказа")
    def test_total_orders_counter_increase(self, order_feed_page, authenticated_user, main_page):
        with allure.step("Получить начальное значение общего счетчика заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            initial_total = order_feed_page.get_total_orders_count()

        with allure.step("Создать новый заказ"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()
            # Ждем обработки заказа через ожидание элемента
            main_page.wait.wait_for_element_visible(main_page.locators.ORDER_MODAL)

        with allure.step("Перейти в ленту заказов и проверить счетчик"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()

            new_total = order_feed_page.get_total_orders_count()
            assert new_total > initial_total, f"Счетчик 'Выполнено за всё время' должен увеличиться. Было: {initial_total}, Стало: {new_total}"

    @allure.title("TC-08: Увеличение счетчика 'Выполнено за сегодня' при новом заказе")
    @allure.description("Тест проверяет увеличение дневного счетчика заказов после создания нового заказа")
    def test_today_orders_counter_increase(self, order_feed_page, authenticated_user, main_page):
        with allure.step("Получить начальное значение дневного счетчика заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            initial_today = order_feed_page.get_today_orders_count()

        with allure.step("Создать новый заказ"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()
            main_page.wait.wait_for_element_visible(main_page.locators.ORDER_MODAL)

        with allure.step("Перейти в ленту заказов и проверить счетчик"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()

            new_today = order_feed_page.get_today_orders_count()
            assert new_today > initial_today, f"Счетчик 'Выполнено за сегодня' должен увеличиться. Было: {initial_today}, Стало: {new_today}"

    @allure.title("TC-09: Появление номера заказа в разделе 'В работе'")
    @allure.description("Тест проверяет отображение номера нового заказа в разделе 'В работе'")
    def test_order_appears_in_progress_section(self, order_feed_page, authenticated_user, main_page, order_modal):
        with allure.step("Создать новый заказ и получить его номер"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()

            # Получаем номер заказа из модального окна
            order_number = order_modal.get_order_number()
            assert order_number is not None, "Не удалось получить номер заказа"

            # Закрываем модальное окно заказа
            order_modal.close_modal()

        with allure.step("Перейти в ленту заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()

        with allure.step("Проверить отображение заказа в разделе 'В работе'"):
            orders_in_progress = order_feed_page.get_orders_in_progress()
            assert order_number in orders_in_progress, f"Заказ {order_number} должен отображаться в разделе 'В работе'. Найдены заказы: {orders_in_progress}"

    @allure.title("TC-10: Отображение нового заказа в общей ленте")
    @allure.description("Тест проверяет отображение нового заказа в основной ленте заказов")
    def test_order_appears_in_feed(self, order_feed_page, authenticated_user, main_page, order_modal):
        with allure.step("Создать новый заказ и получить его номер"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.create_test_order()

            # Получаем номер заказа из модального окна
            order_number = order_modal.get_order_number()
            assert order_number is not None, "Не удалось получить номер заказа"

            # Закрываем модальное окно заказа
            order_modal.close_modal()

        with allure.step("Перейти в ленту заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()
            order_feed_page.wait.wait_for_page_load()

        with allure.step("Проверить отображение заказа в ленте"):
            all_orders = order_feed_page.get_all_visible_orders()
            assert order_number in all_orders, f"Заказ {order_number} должен отображаться в ленте заказов. Найдены заказы: {all_orders}"

    @allure.title("TC-11: Обновление счетчиков в реальном времени")
    @allure.description("Тест проверяет корректность работы счетчиков заказов")
    def test_order_counters_correctness(self, order_feed_page):
        with allure.step("Перейти в ленту заказов"):
            order_feed_page.open()
            order_feed_page.wait_for_page_loaded()

        with allure.step("Проверить корректность счетчиков"):
            total_orders = order_feed_page.get_total_orders_count()
            today_orders = order_feed_page.get_today_orders_count()

            assert total_orders >= 0, "Счетчик 'Выполнено за всё время' должен быть неотрицательным"
            assert today_orders >= 0, "Счетчик 'Выполнено за сегодня' должен быть неотрицательным"
            assert total_orders >= today_orders, "Общее количество заказов не может быть меньше дневного"

    @allure.title("TC-12: Навигация между лентой заказов и конструктором")
    @allure.description("Тест проверяет возможность перехода между разделами")
    def test_feed_constructor_navigation(self, order_feed_page, main_page):
        with allure.step("Перейти из конструктора в ленту заказов"):
            main_page.open()
            main_page.wait_for_main_page_loaded()
            main_page.click_order_feed()
            assert order_feed_page.is_order_feed_active()

        with allure.step("Вернуться в конструктор из ленты заказов"):
            main_page.click_constructor()
            assert main_page.is_main_page_loaded()
