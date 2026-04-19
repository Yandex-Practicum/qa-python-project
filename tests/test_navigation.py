import allure
from pages.main_page import MainPage
from pages.constructor_page import ConstructorPage
from pages.modal_page import ModalPage


@allure.title("Переход в Конструктор")
def test_go_to_constructor(driver):

    page = MainPage(driver)

    with allure.step("Клик Конструктор"):
        page.go_to_constructor()

    with allure.step("Проверка открытия"):
        assert page.is_open()


@allure.title("Переход в Ленту заказов")
def test_go_to_feed(driver):

    page = MainPage(driver)

    with allure.step("Клик Лента заказов"):
        page.go_to_feed()

    with allure.step("Проверка открытия"):
        assert "feed" in driver.current_url


@allure.title("Открытие модального окна ингредиента")
def test_open_modal(driver):

    page = ConstructorPage(driver)
    modal = ModalPage(driver)

    page.go_to_ingredient()

    assert modal.is_open()


@allure.title("Закрытие модального окна")
def test_close_modal(driver):

    page = ConstructorPage(driver)
    modal = ModalPage(driver)

    page.go_to_ingredient()

    modal.close()

    assert modal.wait_closed()
    assert not modal.is_open()