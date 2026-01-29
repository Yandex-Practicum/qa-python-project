from praktikum.bun import Bun
from input_data import Data


class TestBun:

    def test_get_name_true_str(self):
        bun = Bun(Data.BLACK_BUN_NAME, Data.BLACK_BUN_PRICE)
        assert isinstance(bun.get_name(), str)
        assert bun.get_name() == Data.BLACK_BUN_NAME

    def test_get_price_true_float(self):
        bun = Bun(Data.BLACK_BUN_NAME, Data.BLACK_BUN_PRICE)
        assert bun.get_price() == Data.BLACK_BUN_PRICE




