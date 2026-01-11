import pytest

from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        'bun',
        [
            'black bun',
            'white bun',
            'red bun'
        ]
    )
    def test_get_name_true(self, bun):
        bun = Bun(bun, 100)
        bun1 = bun.__dict__

        assert bun.name == bun1['name']
        assert bun.get_name() == bun1['name']

    @pytest.mark.parametrize(
        'price',
        [
            100,
            200,
            300
        ]
    )
    def test_get_price_true(self, price):
        bun = Bun("black bun", price)

        assert bun.price == price
        assert bun.get_price() == price
