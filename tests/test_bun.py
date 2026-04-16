import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("sesame bun", 150.5),
    ])
    def test_get_name_returns_correct_name(self, name, price):
        #Проверяем, что get_name возвращает правильное название булочки
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("sesame bun", 150.5),
    ])
    def test_get_price_returns_correct_price(self, name, price):
        #Проверяем, что get_price возвращает правильную цену булочки
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_bun_initialization(self):
        #Проверяем, что объект Bun создаётся с корректными атрибутами
        bun = Bun("test bun", 99.99)
        assert bun.name == "test bun"
        assert bun.price == 99.99