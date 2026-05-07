import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
    ])
    def test_get_name_returns_name_passed_to_constructor(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100.0),
        ("white bun", 200.5),
        ("red bun", 300.99),
    ])
    def test_get_price_returns_price_passed_to_constructor(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price