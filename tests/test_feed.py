import allure
from pages.feed_page import FeedPage
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.order_modal_page import OrderModalPage


@allure.title("Выполнено за всё время")
def test_total_done(auth_driver):

    feed = FeedPage(auth_driver)
    constructor = ConstructorPage(auth_driver)
    modal = OrderModalPage(auth_driver)
    main = MainPage(auth_driver)

    feed.open_feed()
    before = feed.get_total_done()

    main.go_to_constructor()

    with allure.step("Получить цену до"):
        old_price = constructor.get_total_price()

    with allure.step("Добавить ингредиент"):
        constructor.add_ingredient_to_order()

    with allure.step("Дождаться обновления корзины"):
        constructor.wait_price_changed(old_price)

    with allure.step("Оформить заказ"):
        constructor.place_order()

    feed.open_feed()

    after = feed.get_total_done()

    assert after > before


@allure.title("Выполнено за сегодня")
def test_today_done(auth_driver):

     feed = FeedPage(auth_driver)
     constructor = ConstructorPage(auth_driver)
     modal = OrderModalPage(auth_driver)
     main = MainPage(auth_driver)

     feed.open_feed()
     before = feed.get_today_done()

     main.go_to_constructor()

     with allure.step("Получить цену до"):
        old_price = constructor.get_total_price()

     with allure.step("Добавить ингредиент"):
        constructor.add_ingredient_to_order()

     with allure.step("Дождаться обновления корзины"):
        constructor.wait_price_changed(old_price)

     with allure.step("Оформить заказ"):
        constructor.place_order()

     modal.get_order_number()

     feed.open_feed()
     after = feed.get_today_done()

     assert after > before


@allure.title("После оформления заказа его номер появляется в разделе «В работе»")
def test_order_in_progress(auth_driver):

    feed = FeedPage(auth_driver)
    constructor = ConstructorPage(auth_driver)
    modal = OrderModalPage(auth_driver)
    main = MainPage(auth_driver)

    main.go_to_constructor()

    with allure.step("Получить цену до"):
        old_price = constructor.get_total_price()

    with allure.step("Добавить ингредиент"):
        constructor.add_ingredient_to_order()

    with allure.step("Дождаться обновления корзины"):
        constructor.wait_price_changed(old_price)

    with allure.step("Оформить заказ"):
        constructor.place_order()

    number = modal.get_order_number()

    feed.open_feed()

    assert feed.order_exists(number)