import allure

from praktikum.bun import Bun


class TestBun:
    @allure.title('Проверка названия булки')
    def test_get_name(self):
        bun = Bun("Булочка", 9.99)
        assert bun.get_name() == "Булочка"

    @allure.title('Проверка цены булки')
    def test_get_price(self):
        bun = Bun("Булочка", 9.99)
        assert bun.get_price() == 9.99
