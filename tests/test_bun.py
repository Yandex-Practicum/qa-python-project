import pytest
from praktikum.bun import Bun


class TestBun:
    
    def test_get_name_returns_correct_name(self):
        bun = Bun("Краторная булка N-200i", 1255)
        actual_name = bun.get_name()
        assert actual_name == "Краторная булка N-200i"
    
    def test_get_price_returns_correct_price(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        actual_price = bun.get_price()
        assert actual_price == 988
    
    @pytest.mark.parametrize("name", [
        "Краторная булка N-200i",
        "Флюоресцентная булка R2-D3",
        "Специальная космическая булка",
        "",
        "Очень длинное название булочки для бургера"
    ])
    def test_bun_initialization_with_different_names(self, name):
        bun = Bun(name, 100)
        actual_name = bun.get_name()
        assert actual_name == name
    
    @pytest.mark.parametrize("price", [
        1255,
        988,
        1500,
        0,
        999.99
    ])
    def test_bun_initialization_with_different_prices(self, price):
        bun = Bun("Тестовая булка", price)
        actual_price = bun.get_price()
        assert actual_price == price
    
    def test_bun_initialization_and_retrieval(self):
        expected_name = "Тестовая булка"
        expected_price = 1000
        
        bun = Bun(expected_name, expected_price)
        
        actual_name = bun.get_name()
        actual_price = bun.get_price()
        
        assert actual_name == expected_name
        assert actual_price == expected_price