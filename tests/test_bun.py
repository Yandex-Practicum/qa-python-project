import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name", [
        "Флюоресцентная булка",  
        "black bun",             
        "Спец-булка! №1",        
        ""                       
    ])
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100.0)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [
        100.5,   
        0.0,     
        100,     
        -50.5    
    ])
    def test_get_price_returns_correct_price(self, price):
        bun = Bun("Обычная булка", price)
        assert bun.get_price() == price
