import pytest
from practikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 988.01),
        ("Краторная булка N-200i", 1255.00),
        ("Базовая булка 1337", 420.88)
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name and type(bun.get_name()) == str
    @pytest.mark.parametrize("name, price", [
        ("Флюоресцентная булка R2-D3", 988.01),
        ("Краторная булка N-200i", 1255.00),
        ("Базовая булка 1337", 420.88)
    ])
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price and type(bun.get_price()) == float

