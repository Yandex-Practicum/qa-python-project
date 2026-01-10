import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, price",[
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300)])

    def test_bun_initialization(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self):
        test_name = "black bun"
        bun = Bun(test_name, 100.0)
        assert bun.get_name() == test_name

    def test_get_price(self):
        test_price = 200.00
        bun = Bun("white bun", test_price)
        assert bun.get_price() == test_price