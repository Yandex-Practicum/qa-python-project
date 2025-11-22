import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("bun_name", ["", "black bun", "white bun", "red bun"])
    def test_bun_init_name_check(self, bun_name):
        bun = Bun(name=bun_name, price=0)
        assert bun.name == bun_name

    @pytest.mark.parametrize("bun_price", [100, 199.99, 300.0])
    def test_bun_init_price_check(self, bun_price):
        bun = Bun(name="", price=bun_price)
        assert bun.price == bun_price

    @pytest.mark.parametrize("bun_name", ["", "black bun", "white bun", "red bun"])
    def test_bun_get_name_check(self, bun_name):
        bun = Bun(name=bun_name, price=0)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_price", [100, 199.99, 300.0])
    def test_bun_get_price_check(self, bun_price):
        bun = Bun(name="", price=bun_price)
        assert bun.get_price() == bun_price
