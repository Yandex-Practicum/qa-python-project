import pytest

from data import BunData
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize('name, price', [BunData.buns_list[0],
                                             BunData.buns_list[2]])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [BunData.buns_list[0],
                                             BunData.buns_list[2]])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

