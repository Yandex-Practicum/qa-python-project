from praktikum.bun import Bun
from data import data


class TestBun:
    def test_create_bun_sets_name(self):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.name == data.bun_name

    def test_create_bun_sets_price(self):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.price == data.bun_price

    def test_get_name_returns_correct_name(self):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.get_name() == data.bun_name

    def test_get_price_returns_correct_price(self):
        bun = Bun(data.bun_name, data.bun_price)
        assert bun.get_price() == data.bun_price