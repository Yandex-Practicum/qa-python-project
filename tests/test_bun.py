import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name", ["black bun", "white bun", "red bun"])
    def test_bun_creation_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_bun_creation_price(self, price):
        bun = Bun("some name", price)
        assert bun.get_price() == price

class TestBunNegative:
    
    @pytest.mark.parametrize("name", ["", None])
    def test_bun_negative_name(self, name):
        bun = Bun(name, 100) 
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [-50, 0])
    def test_bun_negative_price(self, price):
        bun = Bun("some bun", price)
        assert bun.get_price() == price
