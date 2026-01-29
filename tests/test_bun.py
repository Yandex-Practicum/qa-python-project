from data import DataBun
from praktikum.bun import Bun


class TestBun:
    def test_get_name_checking_name(self):
        name, price = DataBun.get_data_bun()
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name

    def test_get_price_checking_price(self):
        name, price = DataBun.get_data_bun()
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price
