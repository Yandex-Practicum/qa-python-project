import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", [
        "Краторная булка N-200i",
        "Флюоресцентная булка R2-D3",
        "Мини-булка",
    ])
    def test_get_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize("price", [1255, 988, 0])
    def test_get_price(self, price):
        bun = Bun("Тестовая булка", price)
        assert bun.get_price() == price