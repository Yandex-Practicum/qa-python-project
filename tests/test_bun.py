import pytest
from praktikum.bun import Bun
from data.data import BUN_NAMES_DATA, BUN_PRICES_DATA

class TestBun:
    @pytest.mark.parametrize("name", BUN_NAMES_DATA)
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", BUN_PRICES_DATA)
    def test_get_price_returns_correct_price(self, price):
        bun = Bun("Булка", price)
        assert bun.get_price() == price