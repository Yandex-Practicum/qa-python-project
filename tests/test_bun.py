import pytest
from praktikum.bun import Bun


class TestBun:
    
    def test_get_name(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_name() == "Краторная булка N-200i"
    
    def test_get_price(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        assert bun.get_price() == 988
    
    @pytest.mark.parametrize("name", [
        "Краторная булка N-200i",
        "Флюоресцентная булка R2-D3",
        "Специальная космическая булка",
        "",
        "Очень длинное название булочки для бургера"
    ])
    def test_bun_initialization_with_different_names(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize("price", [
        1255,
        988,
        1500,
        0,
        999.99
    ])
    def test_bun_initialization_with_different_prices(self, price):
        bun = Bun("Тестовая булка", price)
        assert bun.get_price() == price