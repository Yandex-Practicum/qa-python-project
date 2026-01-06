import pytest
from praktikum.bun import Bun
from data import BunData


class TestBun:
    @pytest.mark.parametrize('name, price', BunData)
    def test_bun_constructor(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize('name, price', BunData)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', BunData)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
