from data import DataBun
from praktikum.bun import Bun


class TestBun:
    def test_add_new_name_bun_should_be_added(self):
        bun = Bun(DataBun.NAME_BUN, DataBun.PRICE_BUN)

        assert bun.get_name() == DataBun.NAME_BUN

    def test_get_price_received(self):
        bun = Bun(DataBun.NAME_BUN, DataBun.PRICE_BUN)

        assert bun.get_price() == DataBun.PRICE_BUN

