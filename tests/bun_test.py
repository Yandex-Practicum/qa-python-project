import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', ['black bun', 'white bun', ''])
    def test_get_name_returns_name(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [100, 0, 99.5])
    def test_get_price_returns_price(self, price):
        bun = Bun('black bun', price)

        assert bun.get_price() == price
