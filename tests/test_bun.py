from praktikum.bun import Bun
import pytest


class TestBun:
    @pytest.mark.parametrize('name', ["Имя", "Name", "1111", " ", "@@@@"])
    def test_get_bun_name(self, name):
        bun = Bun(name, 10)
        
        assert bun.get_name() == name
    
    @pytest.mark.parametrize('price', [0, 0.0001, 1, 999999.999, " ", -9])
    def test_get_bun_price(self, price):
        bun = Bun('name', price)
        assert bun.get_price() == price