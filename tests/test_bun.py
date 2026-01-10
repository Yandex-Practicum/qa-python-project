from praktikum.bun import Bun
from data import Data

class TestBun:
    def test_get_name(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        name = bun.get_name()

        assert name == 'black bun'

    def test_get_price(self):
        bun = Bun(Data.bun_name, Data.bun_price)
        price = bun.get_price()

        assert price == 10
