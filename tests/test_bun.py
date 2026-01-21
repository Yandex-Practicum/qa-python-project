from data import Data


class TestBun:

    def test_get_name(self, new_bun):
        assert new_bun.get_name() == Data.BUN_NAME

    def test_get_price(self, new_bun):
        assert new_bun.get_price() == Data.BUN_PRICE
