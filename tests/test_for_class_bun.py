import pytest
from data_for_tests.data_for_buns import DataBuns
from praktikum.bun import Bun

class TestBun:
   
    @pytest.mark.parametrize('name, price', DataBuns.buns)
    def test_bun_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

     
    @pytest.mark.parametrize('name, price', DataBuns.buns)
    def test_bun_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price