import pytest
from ..bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', [('Флюоресцентная булка R2-D3'), ('Краторная булка N-200i')])
    def test_name(self, name):
        bun = Bun(name, None)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [(988.8), (1255.5)])
    def test_price(self, price):
        bun = Bun(None, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name', [('Флюоресцентная булка R2-D3'), ('Краторная булка N-200i')])
    def test_name_type(self, name):
        bun = Bun(name, None)
        assert type(bun.get_name()) is str

    @pytest.mark.parametrize('price', [(988.8), (1255.5)])
    def test_price_type(self, price):
        bun = Bun(None, price)
        assert type(bun.get_price()) is float
