import data
from praktikum.bun import Bun


class TestBun:

    def test_get_name(self):
       bun = Bun(data.bun_name, data.bun_price)
       assert bun.get_name() == data.bun_name

    def test_get_price(self):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.get_price() == data.bun_price



