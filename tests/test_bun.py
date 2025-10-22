import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("free bun", 0),
            ("float price", 99.99),
        ],
    )
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
            ("free bun", 0),
            ("float price", 99.99),
        ],
    )
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
