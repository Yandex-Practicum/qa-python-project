from data import *
from praktikum.bun import Bun

class TestBun:
    def test_bun_init(self):
        name = get_random_value(BUNS_NAMES)
        price = get_random_value(PRICES)
        bun = Bun(name, price)

        assert bun.get_price() == price and bun.get_name() == name
