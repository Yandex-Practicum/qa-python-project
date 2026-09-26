import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        'name',
        [
            'Black bun',
            'White bun',
            'Red bun',
        ]
    )
    def test_get_name_returns_correct_name(self, name):
        bun = Bun(name, 100)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        'price',
        [
            100,
            200.5,
            0,
        ]
    )
    def test_get_price_returns_correct_price(self, price):
        bun = Bun('Black bun', price)

        assert bun.get_price() == price