from praktikum.bun import Bun
from test_data import BUN_NAME, BUN_PRICE

class TestBun:

    def test_get_name_returns_correct_name(self, bun: Bun):
        assert bun.get_name() == BUN_NAME

    def test_get_price_returns_correct_price(self, bun: Bun):
        assert bun.get_price() == BUN_PRICE
