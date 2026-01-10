import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name,price", [
        ("Краторная булка", 200),
        ("Флюоресцентная булка", 150),
        ("Булка", 99.99),
    ])
    def test_bun_get_name_and_get_price(self, name, price):
        """Тестируем только через публичные методы get_name() и get_price()"""
        bun = Bun(name, price)

        # Только публичные методы, без доступа к атрибутам
        assert bun.get_name() == name
        assert bun.get_price() == price