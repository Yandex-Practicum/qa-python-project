import pytest

from data import Data
from praktikum.bun import Bun

class TestBun:
    buns = [
        (bun['name'], bun['price']) for bun in Data.BUNS
    ]
    @pytest.mark.parametrize('name, price', buns)
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        actual_name = bun.get_name()
        expected_name = name

        assert actual_name == expected_name

    @pytest.mark.parametrize('name, price', buns)
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        actual_price = bun.get_price()
        expected_price = price

        assert actual_price == expected_price

    @pytest.mark.parametrize('name, price', buns)
    def test_name_is_str(self, name, price):
        bun = Bun(name, price)
        actual_name = bun.get_name()

        assert isinstance(actual_name, str)

    @pytest.mark.parametrize('name, price', buns)
    def test_price_is_float_when_set_float(self, name, price):
        name = 'Улетная булка'
        price = 100.5
        bun = Bun(name, price)
        actual_price = bun.get_price()

        assert isinstance(actual_price, float)
