import pytest
from src.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("special bun", 150.5),
    ])
    def test_bun_creation(self, name, price):
        """Тест создания булочки с разными параметрами"""
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_get_name(self):
        """Тест получения названия булочки"""
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"
        assert isinstance(bun.get_name(), str)

    def test_bun_get_price(self):
        """Тест получения цены булочки"""
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100


    def test_bun_price_type(self):
        """Проверка типа цены булочки"""
        bun = Bun("test bun", 150.75)
        assert isinstance(bun.price, float)