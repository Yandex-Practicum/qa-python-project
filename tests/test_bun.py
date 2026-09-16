import pytest
from ..bun import Bun


class TestBun:

    def test_init(self):
        bun = Bun("Black Bun", 100.0)
        assert bun.get_name() == "Black Bun"
        assert bun.get_price() == 100.0

    @pytest.mark.parametrize("name,price,expected_name,expected_price", [
        ("Black Bun", 100.0, "Black Bun", 100.0),
        ("White Bun", 200.0, "White Bun", 200.0),
        ("Red Bun", 300.0, "Red Bun", 300.0),
        ("", 0.0, "", 0.0),
        ("Special Bun", 999.99, "Special Bun", 999.99),
    ])
    def test_get_name_and_price(self, name, price, expected_name, expected_price):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_negative_price(self):
        bun = Bun("Free Bun", -10.0)
        assert bun.get_price() == -10.0

    def test_none_name(self):
        bun = Bun(None, 100.0)
        assert bun.get_name() is None
