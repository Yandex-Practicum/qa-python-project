import pytest
import data as D
from praktikum.bun import Bun



class TestBun:

    @pytest.mark.parametrize('name, price', D.BUN_PARAMS)
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_name(self, bun):
        assert bun.get_name() == D.BURGER_BUN_NAME

    def test_get_price(self, bun):
        assert bun.get_price() == D.BURGER_BUN_PRICE