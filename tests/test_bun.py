import pytest
from data import buns


class TestBun:

    @pytest.mark.parametrize('bun_data', buns)
    def test_get_name(self, bun, bun_data):
        bun.name = bun_data['name']

        assert bun.get_name() == bun.name

    @pytest.mark.parametrize('bun_data', buns)
    def test_get_price(self, bun, bun_data):
        bun.price = bun_data['price']

        assert bun.get_price() == bun.price
