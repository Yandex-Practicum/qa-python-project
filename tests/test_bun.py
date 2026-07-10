import pytest
from bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988),
        ("Простая булка", 50)
    ])
    def test_bun_creation(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_get_name_returns_string(self):
        bun = Bun("Тестовая булка", 100)
        name = bun.get_name()
        assert isinstance(name, str)
        assert name == "Тестовая булка"

    def test_bun_get_price_returns_number(self):
        bun = Bun("Тестовая булка", 100)
        price = bun.get_price()
        assert isinstance(price, (int, float))
        assert price == 100

    def test_bun_price_can_be_float(self):
        bun = Bun("Тестовая булка", 99.99)
        assert bun.get_price() == 99.99
        assert isinstance(bun.get_price(), float)