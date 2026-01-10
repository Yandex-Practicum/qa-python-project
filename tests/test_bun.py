import pytest
from praktikum.bun import Bun
from data import buns_data


class TestBun:

    @pytest.mark.parametrize("bun_data", buns_data)
    def test_get_name(self, bun_data):
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_name() == bun_data['name']

    @pytest.mark.parametrize("bun_data", buns_data)
    def test_get_price(self, bun_data):
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_price() == bun_data['price']
