import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('name, price', [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)])
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        bun_name = bun.get_name()
        assert bun_name == name

    @pytest.mark.parametrize('name, price', [('Флюоресцентная булка R2-D3', 988), ('Краторная булка N-200i', 1255)])
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        bun_price = bun.get_price()
        assert bun_price == price