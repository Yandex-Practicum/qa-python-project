import pytest
import sys
sys.path.append("..")
from bun import Bun
from data import DataBun

class TestBun:
    @pytest.mark.parametrize('name, price', [(DataBun.BUN_FIRST, DataBun.BUN_FIRST_PRICE), (DataBun.BUN_SECOND, DataBun.BUN_SECOND_PRICE)])
    def test_bun_creation_name(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name

    @pytest.mark.parametrize('name, price', [(DataBun.BUN_FIRST, DataBun.BUN_FIRST_PRICE), (DataBun.BUN_SECOND, DataBun.BUN_SECOND_PRICE)])
    def test_bun_creation_price(self, name, price):
        bun = Bun(name, price)
        assert bun.price == price

    @pytest.mark.parametrize('name, price', [(DataBun.BUN_FIRST, DataBun.BUN_FIRST_PRICE), (DataBun.BUN_SECOND, DataBun.BUN_SECOND_PRICE)])
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [(DataBun.BUN_FIRST, DataBun.BUN_FIRST_PRICE), (DataBun.BUN_SECOND, DataBun.BUN_SECOND_PRICE)])
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
