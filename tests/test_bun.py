from data import Data
from praktikum.bun import Bun


class TestBun:
    def test_get_name(self):
        new_bun = Bun(Data.BunName, Data.BumPrice)
        assert new_bun.get_name() == Data.BunName


    def test_get_price(self):
        new_price = Bun(Data.BunName, Data.BumPrice)
        assert new_price.get_price() == Data.BumPrice