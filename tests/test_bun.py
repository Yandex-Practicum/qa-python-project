import pytest
import allure
from Diplom_1.bun import Bun


class TestBun:
    @allure.title('Проверка создания объекта с правильными атрибутами')
    @pytest.mark.parametrize("name, price", [
        ("Classic Bun", 199),
        ("Sesame Bun", 249),
        ("Gluten-Free Bun", 300)
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    @allure.title('Тест метода get_name')
    def test_get_name(self, bun_fixture):
        assert bun_fixture.get_name() == "Classic Bun"

    @allure.title('Тест метода get_price')
    def test_get_price(self, bun_fixture):
        assert bun_fixture.get_price() == 199

    @allure.title('Проверка изменения названия булочки')
    def test_set_name(self, bun_fixture):
        bun_fixture.name = "Updated Bun"
        assert bun_fixture.get_name() == "Updated Bun"

    @allure.title('Проверка изменения цены булочки')
    def test_set_price(self, bun_fixture):
        bun_fixture.price = 255
        assert bun_fixture.get_price() == 255

    @allure.title('Негативная Проверка на поле Имя: значение name не является строкой')
    @pytest.mark.parametrize("invalid_name, price", [
        (1, 199),
        (None, 599),
    ])
    def test_bun_creation_with_invalid_name(self, invalid_name, price):
        bun = Bun(invalid_name, price)
        assert not isinstance(bun.get_name(), (str))

    @allure.title('Негативная Проверка на поле Цена: значение цены не числовым')
    @pytest.mark.parametrize("name, invalid_price", [
        ("Classic Bun", "not a number"),
        ("Sesame Bun", None),
    ])
    def test_bun_creation_with_invalid_price(self, name, invalid_price):
        bun = Bun(name, invalid_price)
        assert not isinstance(bun.get_price(), (int, float))

    @allure.title('Негативная проверка поля Цена: отрицательные и не отрицательное числа')
    @pytest.mark.parametrize("price", [-10, 0, -55])
    def test_invalid_price(self, price):
        bun = Bun(name="Invalid Bun", price=price)
        assert bun.price == price
        assert bun.price <= 0
