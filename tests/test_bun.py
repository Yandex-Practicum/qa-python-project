from .. data import Helpers
from ..praktikum.bun import Bun


class TestBun:

    def test_create_new_bun_(self):
        new_bun = Bun(Helpers.BUN_NAME, Helpers.BUN_PRICE)
        assert new_bun.get_name() == Helpers.BUN_NAME


    def test_create_new_bun_price(self):
        new_bun = Bun(Helpers.BUN_NAME, Helpers.BUN_PRICE)
        assert new_bun.get_price() == Helpers.BUN_PRICE