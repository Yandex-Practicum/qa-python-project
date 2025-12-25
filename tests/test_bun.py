from praktikum.bun import Bun
from data import BUN_NAME, BUN_PRICE


class TestBun:

    def test_bun_init(self):
        bun = Bun(BUN_NAME, BUN_PRICE)

        assert bun.name == BUN_NAME and BUN_PRICE

    def test_get_name_bun(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        new_name = bun.get_name()

        assert new_name == BUN_NAME

    def test_get_price_bun(self):
        bun = Bun(BUN_NAME, BUN_PRICE)
        new_price = bun.get_price()

        assert new_price == BUN_PRICE

