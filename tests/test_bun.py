from praktikum.bun import Bun
from test_data.test_data import BLACK_BUN_NAME, BLACK_BUN_PRICE


class TestBun:
    def test_bun_init_name(self):
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        assert bun.name

    def test_bun_init_price(self):
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        assert bun.price

    def test_bun_get_name_correct(self):
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        bun_name = BLACK_BUN_NAME
        assert bun.get_name() == bun_name

    def test_bun_get_price_correct(self):
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        bun_price = BLACK_BUN_PRICE
        assert bun.get_price() == bun_price
