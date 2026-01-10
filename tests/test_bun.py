import pytest
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize('bun_name', ['Булка', 'БУЛКА', 'булка', '123', 'Булка_123'])
    def test_get_bun_name(self, bun_name):
        bun = Bun(bun_name, 50.0)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize('bun_price', [0, -1, 1, 1.0, 123.45])
    def test_get_bun_price(self, bun_price):
        bun = Bun('Булочка', bun_price)
        assert bun.get_price() == bun_price
