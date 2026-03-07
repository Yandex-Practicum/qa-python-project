import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("super bun", 99.9)
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self, black_bun):
        assert black_bun.get_name() == "black bun"

    def test_get_price(self, black_bun):
        assert black_bun.get_price() == 100