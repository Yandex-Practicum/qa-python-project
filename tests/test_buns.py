from praktikum.bun import Bun
from data import bun_data


class TestBuns:

    def test_get_name_bun(self):
        bun = Bun(bun_data[0], None)
        assert bun.get_name() == bun_data[0]

    def test_get_price_bun(self):
        bun = Bun(None, bun_data[1])
        assert bun.get_price() == bun_data[1]