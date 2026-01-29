from praktikum.bun import Bun

from data import DataBun


class TestBun:
    def test_name_bun_true(self):
        bun = Bun(DataBun.NAME_BUN, DataBun.PRICE_BUN)
        assert bun.get_name() == DataBun.NAME_BUN

    def test_price_bun_true(self):
        bun = Bun(DataBun.NAME_BUN, DataBun.PRICE_BUN)
        assert bun.get_price() == DataBun.PRICE_BUN