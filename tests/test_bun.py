import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize('name', [
        'black bun',
        'white bun',
        'red bun',
    ])
    def test_get_name(self, name):
        bun = Bun(name, 100)
        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [
        100,
        200.5,
        0,
    ])
    def test_get_price(self, price):
        bun = Bun('test bun', price)
        assert bun.get_price() == price