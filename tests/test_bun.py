import pytest
from ..bun import Bun


class TestBun:

    def test_init(self):
        bun = Bun("Black Bun", 100.0)
        assert bun.get_name() == "Black Bun"
        assert bun.get_price() == 100.0

    @pytest.mark.parametrize("name,expected_name", [
        ("Black Bun", "Black Bun"),
        ("White Bun", "White Bun"),
        ("Red Bun", "Red Bun"),
        ("", ""),
        ("Special Bun", "Special Bun"),
    ])
    def test_get_name(self, name, expected_name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("price,expected_price", [
        (100.0, 100.0),
        (200.0, 200.0),
        (300.0, 300.0),
        (0.0, 0.0),
        (999.99, 999.99),
    ])
    def test_get_price(self, price, expected_price):
        bun = Bun("Test Bun", price)
        assert bun.get_price() == expected_price

    def test_none_name(self):
        bun = Bun(None, 100.0)
        assert bun.get_name() is None
