import pytest
from praktikum.bun import Bun
from data import Data

class TestBun:

    @pytest.mark.parametrize('name, price', [
        (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
        (Data.RED_BUN, Data.RED_BUN_PRICE),
        (Data.WHITE_BUN, Data.WHITE_BUN_PRICE)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (Data.BLACK_BUN, Data.BLACK_BUN_PRICE),
        (Data.RED_BUN, Data.RED_BUN_PRICE),
        (Data.WHITE_BUN, Data.WHITE_BUN_PRICE)
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
