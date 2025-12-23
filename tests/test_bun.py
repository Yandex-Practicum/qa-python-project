import pytest
from Prakticum.bun import Bun
from data import Data


class TestBun:

    @pytest.mark.parametrize('name, price', [
        (Data.NEW_FIRST_BUN, Data.NEW_FIRST_BUN_PRICE),
        (Data.NEW_SECOND_BUN, Data.NEW_SECOND_BUN_PRICE)
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        (Data.NEW_FIRST_BUN, Data.NEW_FIRST_BUN_PRICE),
        (Data.NEW_SECOND_BUN, Data.NEW_SECOND_BUN_PRICE)
    ])
    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price