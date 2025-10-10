import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name, price', [['Булочка с корицей', 10], ['Булочка черная', 10], ['Булочка белая', 10]])
    def test_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [['Булочка с корицей', 10.0], ['Булочка черная', 15000.0], ['Булочка белая', 0.0]])
    def test_get_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price


