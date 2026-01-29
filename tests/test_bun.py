from data import BurgerData
from bun import Bun
import pytest


class TestBun:

    def test_get_bun_name(self):
        bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        assert bun.get_name() == BurgerData.BUN_NAME

    @pytest.mark.parametrize('price', [0.0, None])
    def test_none_bun_price(self, price):
        bun = Bun(BurgerData.BUN_NAME, price)
        assert bun.price == price

    def test_get_bun_price(self):
        bun = Bun(BurgerData.BUN_NAME, BurgerData.BUN_PRICE)
        assert bun.get_price() == BurgerData.BUN_PRICE
