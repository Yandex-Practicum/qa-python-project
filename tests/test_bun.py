from Diplom_1.bun import Bun
from data import Data
class TestBun:
    def test_get_name(self, create_bun):
        bun_for_test = create_bun
        assert bun_for_test.get_name() == Data.crater_bun

    def test_get_price(self, create_bun):
        bun_for_test = create_bun
        assert bun_for_test.get_price() == Data.price_3
