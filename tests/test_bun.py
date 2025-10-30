import pytest
from praktikum.bun import Bun


class TestBun:
    
    def test_get_name(self):
        bun = Bun("Краторная булка N-200i", 1255)
        assert bun.get_name() == "Краторная булка N-200i"
    
    def test_get_price(self):
        bun = Bun("Флюоресцентная булка R2-D3", 988)
        assert bun.get_price() == 988
    
    @pytest.mark.parametrize("name,price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("Специальная космическая булка", 1500),
        ("", 0),
        ("Очень длинное название булочки для бургера", 999.99)
    ])
    def test_bun_initialization_with_different_values(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price