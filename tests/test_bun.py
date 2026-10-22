import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    @pytest.mark.parametrize("name, price", [
        ("Краторная булка N-200i", 1255.0),
        ("Флюоресцентная булка R2-D3", 988.0),
        ("Обычная булка", 100.0)
    ])
    def test_bun_get_name(self, name, price):
        """Тест: получение названия булочки"""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("Краторная булка N-200i", 1255.0),
        ("Флюоресцентная булка R2-D3", 988.0),
        ("Обычная булка", 100.0)
    ])
    def test_bun_get_price(self, name, price):
        """Тест: получение цены булочки"""
        bun = Bun(name, price)
        assert bun.get_price() == price