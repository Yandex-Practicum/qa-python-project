import data
from praktikum.bun import Bun


class TestBun:

    def test_get_name_bun_got_correct_name(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_name() == data.BUN_NAME

    def test_get_price_bun_got_correct_price(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_price() == data.BUN_PRICE
