import pytest
from bun import Bun

class TestBun:
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("special bun", 99.99),
    ])
    def test_bun_creation_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("", 0),
        ("special bun", 99.99),
    ])
    def test_bun_creation_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
    
    def test_bun_get_name_returns_correct_value(self):
        bun = Bun("black bun", 100)
        assert bun.get_name() == "black bun"
    
    def test_bun_get_price_returns_correct_value(self):
        bun = Bun("white bun", 200)
        assert bun.get_price() == 200
    
    @pytest.mark.parametrize("price", [0, 0.01, 50, 100.5, 999.99])
    def test_bun_price_accepts_different_values(self, price):
        bun = Bun("test bun", price)
        assert bun.get_price() == price