import pytest
from praktikum.bun import Bun
from data import BunsData

class TestBun:
    @pytest.mark.parametrize("name, price", BunsData.buns_data)
    def test_get_name_bun(self, name, price):
        buns = Bun(name, price)
        assert buns.get_name() == name

    @pytest.mark.parametrize("name, price", BunsData.buns_data)
    def test_get_price_bun(self, name, price):
        buns = Bun(name, price)
        assert buns.get_price() == price