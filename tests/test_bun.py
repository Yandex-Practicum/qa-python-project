import pytest
from praktikum.bun import Bun
from constants import Constants


class TestBun:

    @pytest.mark.parametrize("bun_name,bun_price", Constants.BUNS)
    def test_bun_name(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name

    @pytest.mark.parametrize("bun_name,bun_price", Constants.BUNS)
    def test_bun_price(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.price == bun_price

    @pytest.mark.parametrize("bun_name,bun_price", Constants.BUNS)
    def test_get_name_method(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_name,bun_price", Constants.BUNS)
    def test_get_price_method(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price









