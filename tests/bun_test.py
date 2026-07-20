import pytest
from praktikum.bun import Bun
from data import BUN_DATA1, BUN_DATA2, BUN_DATA3


class TestBun:

    @pytest.mark.parametrize("name, price", [
        (BUN_DATA1["name"], BUN_DATA1["price"]),
        (BUN_DATA2["name"], BUN_DATA2["price"]),
        (BUN_DATA3["name"], BUN_DATA3["price"]),
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_get_name(self):
        bun = Bun(BUN_DATA1['name'], BUN_DATA1['price'])
        assert bun.get_name() == BUN_DATA1['name']

    def test_bun_get_price(self):
        bun = Bun(BUN_DATA2['name'], BUN_DATA2['price'])
        assert bun.get_price() == BUN_DATA2['price']