import pytest
from praktikum.bun import Bun


class TestBun:
    
    def test_bun_creation_name(self):
        bun = Bun("black bun", 100)
        assert bun.name == "black bun"
    
    def test_bun_creation_price(self):
        bun = Bun("black bun", 100)
        assert bun.price == 100
    
    def test_get_name(self):
        bun = Bun("white bun", 200)
        assert bun.get_name() == "white bun"
    
    def test_get_price(self):
        bun = Bun("red bun", 300)
        assert bun.get_price() == 300
    
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300.5),
    ])
    def test_bun_get_name_parametrized(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300.5),
    ])
    def test_bun_get_price_parametrized(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
        