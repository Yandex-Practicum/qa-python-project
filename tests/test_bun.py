import pytest
from pages.bun import Bun


class TestBun:

    def test_constructor_sets_name_and_price(self):
        name = "Test Bun"
        price = 99.9
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_get_name_returns_correct_value(self):
        bun = Bun("Black Bun", 100)
        assert bun.get_name() == "Black Bun"

    def test_get_price_returns_correct_value(self):
        bun = Bun("White Bun", 200)
        assert bun.get_price() == 200