import pytest
from praktikum.bun import Bun
from data import TEST_BUN_DATA

class TestBun:

    @pytest.mark.parametrize("name, expected_name", TEST_BUN_DATA["names"])
    def test_get_name_returns_correct_name(self, name, expected_name):
        """Метод get_name возвращает правильное имя."""
        bun = Bun(name, 100.0)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("price, expected_price", TEST_BUN_DATA["prices"])
    def test_get_price_returns_correct_price(self, price, expected_price):
        """Метод get_price возвращает правильную цену."""
        bun = Bun("Булочка", price)
        assert bun.get_price() == expected_price