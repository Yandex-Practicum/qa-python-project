from praktikum_package.bun import Bun
from data import Data


class TestBun:
    def test_get_name_success(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_name() == Data.BUN_NAME

    def test_get_price_success(self):
        new_bun = Bun(Data.BUN_NAME, Data.BUN_PRICE)
        assert new_bun.get_price() == Data.BUN_PRICE
