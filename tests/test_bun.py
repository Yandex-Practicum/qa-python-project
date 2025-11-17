import pytest
from bun import Bun


class TestBun:
    
    @pytest.mark.parametrize("name,price", [
        ("black bun", 100),
        ("white bun", 200), 
        ("red bun", 300),
        ("", 0),
        ("special bun", 999.99)
    ])
    def test_bun_creation_and_getters(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price