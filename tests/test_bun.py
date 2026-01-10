from data import BurgerSample
from praktikum.bun import Bun


class TestBun:

    def test_get_name_success(self):
        bun = Bun(BurgerSample.BUN_NAME, BurgerSample.BUN_PRICE)
        assert bun.get_name() == BurgerSample.BUN_NAME

    def test_get_price_success(self):
        bun = Bun(BurgerSample.BUN_NAME, BurgerSample.BUN_PRICE)
        assert bun.get_price() == BurgerSample.BUN_PRICE
