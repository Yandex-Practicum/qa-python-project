import pytest
from praktikum.bun import Bun
from static_data import Data


class TestBun:

    # Test for get_name() method
    @pytest.mark.parametrize('name,price', [
        (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
        (Data.WHITE_BUN, Data.WHITE_BUN_PRICE),
        (Data.RED_BUN, Data.RED_BUN_PRICE)
    ])
    def test_method_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Test for get_price() method
    @pytest.mark.parametrize('name,price', [
        (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
        (Data.WHITE_BUN, Data.WHITE_BUN_PRICE),
        (Data.RED_BUN, Data.RED_BUN_PRICE)
    ])
    def test_method_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
