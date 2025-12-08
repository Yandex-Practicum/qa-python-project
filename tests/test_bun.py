import pytest
from data import BunTestData1, BunTestData2
from praktikum.bun import Bun


class TestBun:
    
    @pytest.mark.parametrize('name, price', [
        (BunTestData1.bun_name, BunTestData1.bun_price),
        (BunTestData2.bun_name, BunTestData2.bun_price)
    ])
    def test_bun_constructor_success(self, name, price):
        bun = Bun(name, price)
        assert bun.name == name
        assert bun.price == price

    def test_get_bun_name_check_success(self):
        bun = Bun(BunTestData1.bun_name, BunTestData1.bun_price)
        assert bun.get_name() == BunTestData1.bun_name

    def test_get_bun_price_check_success(self):
        bun = Bun(BunTestData2.bun_name, BunTestData2.bun_price)
        assert bun.get_price() == BunTestData2.bun_price
        
        