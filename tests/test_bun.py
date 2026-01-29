import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('bun_name', ['Былочка', 'BunS', 'bu!nS', '', None, "123"])
    def test_get_name(self, bun_name):
        bun = Bun(bun_name, 10.0)

        assert bun.get_name() == bun_name

    @pytest.mark.parametrize('prices', [10.0, 0.0, 1.7976931348623157e+308, 2.2250738585072014e-308])
    def test_get_price(self, prices):
        bun = Bun("Buns", prices)
        assert bun.get_price() == prices
