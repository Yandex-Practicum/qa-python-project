from praktikum.bun import Bun
from data.bun_data import BunData


class TestBun:

    def test_get_name_get_name_of_bun(self):
        bun = Bun(name= BunData.bun, price= BunData.price)
        assert bun.get_name() == BunData.bun

    def test_get_price_get_name_of_bun(self):
        bun = Bun(name = BunData.bun, price = BunData.price)
        assert bun.get_price() == 2.5 and type(bun.get_price()) == float

