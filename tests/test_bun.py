import pytest

from praktikum.bun import Bun
from data.ingredients import buns


class TestBun:
    @pytest.mark.parametrize('name, price', buns)
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', buns)
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price