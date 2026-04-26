import pytest
from praktikum.bun import Bun

class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize("name,price,expected_name,expected_price", [
        ("black bun", 100, "black bun", 100),
        ("white bun", 200.5, "white bun", 200.5),
        ("red bun", 0, "red bun", 0),
        ("", 50, "", 50),
    ])
    def test_bun_init(self, name, price, expected_name, expected_price):
        """Тест инициализации булочки"""
        bun = Bun(name, price)
        assert bun.name == expected_name
        assert bun.price == expected_price

    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200),
        ("test bun", 150.75),
    ])
    def test_get_name(self, name, price):
        """Тест получения названия булочки"""
        bun = Bun(name, price)
        result = bun.get_name()
        assert result == name

    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 0),
        ("test", 999.99),
    ])
    def test_get_price(self, name, price):
        """Тест получения цены булочки"""
        bun = Bun(name, price)
        result = bun.get_price()
        assert result == price