import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, price, expected_name, expected_price", [
        ("white", 50, "white", 50),
        ("black", -10, "black", -10),
        ("red", 0, "red", 0)
    ])

    def test_bun_initialization(self, name, price, expected_name, expected_price):
        bun = Bun(name, price)
        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    def test_bun_price(self):
        bun = Bun("blue", 100)
        assert bun.get_price() == 100

    def test_bun_name(self):
        bun = Bun("green", 150)
        assert bun.get_name() == "green"
