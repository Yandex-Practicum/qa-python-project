
from praktikum_app.data import Data
from src.bun import Bun


class TestBun:
    def test_get_bun_name(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_name() == Data.BUN_NAME

    def test_get_bun_price(self):
        bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert bun.get_price() == Data.BUN_PRICE
