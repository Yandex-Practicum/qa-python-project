import pytest
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"

    def test_get_price(self):
        bun = Bun("black bun", 100)
        assert bun.get_price() == 100

    @pytest.mark.parametrize("name,price", [
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("special bun", 999.99)
    ])
    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price