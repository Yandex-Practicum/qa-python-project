import pytest
from practikum.bun import Bun


class TestBun:
    def test_bun_creation(self):
        bun = Bun("Sesame", 1.5)

        assert bun.get_name() == "Sesame" and bun.get_price() == 1.5

    def test_bun_negative_price(self):
        bun = Bun("Whole Wheat", -0.5)

        assert bun.get_price() == -0.5

    @pytest.mark.parametrize("name, price", [
        ("", 1.0), ("Sesame", -1.0)
    ])
    def test_bun_invalid_data(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
