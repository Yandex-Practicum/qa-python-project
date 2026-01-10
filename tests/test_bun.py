import pytest

from ..bun import Bun


class TestBun:
    @pytest.mark.parametrize('name', [('bun'), ('bigbun')])
    def test_init_name(self, name):
        bun = Bun(name, None)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [(10), (1.5)])
    def test_init_price(self, price):
        bun = Bun(None, price)
        assert bun.get_price() == price

    @pytest.mark.parametrize('name, price', [('bun', 10), ('bigbun', 1.5)])
    def test_check_type_name(self, name, price):
        bun = Bun(name, price)
        assert type(bun.get_name()) is str
        assert bun.get_name() is name

    @pytest.mark.parametrize('name, price', [('bigbun', 1.5), ('bun', 10.0)])
    def test_check_type_price(self, name, price):
        bun = Bun(name, price)
        assert type(bun.get_price()) is float
        assert bun.get_price() == price


class TestNegativeBun:
    @pytest.mark.parametrize('name, price', [(123, None)])
    def test_negative_check_type_name(self, name, price):
        bun = Bun(name, price)
        assert type(bun.get_name()) is not str

    @pytest.mark.parametrize('name, price', [(None, 1)])
    def test_negative_check_type_price(self, name, price):
        bun = Bun(name, price)
        assert type(bun.get_price()) is not float

