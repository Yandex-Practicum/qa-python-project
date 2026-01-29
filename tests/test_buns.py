from praktikum.bun import Bun
from data import bun_price, bun_name
class TestBuns:
    def test_get_bun_name(self):
        bun = Bun(bun_name, bun_price)

        assert bun.get_name() == bun_name

    def test_get_bun_price(self):
        bun = Bun(bun_name, bun_price)

        assert bun.get_price() == bun_price

