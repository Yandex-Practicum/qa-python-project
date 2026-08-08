import pytest
from praktikum.bun import Bun
from data import BunTestData


class TestBun:

    @pytest.mark.parametrize("bun_data", [
        BunTestData.VALID_BUN,
        BunTestData.VALID_BUN_2,
        BunTestData.EMPTY_NAME_BUN,
    ])
    def test_bun_creation(self, bun_data):
        bun = Bun(bun_data["name"], bun_data["price"])
        assert bun.get_name() == bun_data["name"]
        assert bun.get_price() == bun_data["price"]

    def test_bun_get_name(self):
        bun_data = BunTestData.VALID_BUN
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_name() == bun_data['name']

    def test_bun_get_price(self):
        bun_data = BunTestData.VALID_BUN_2
        bun = Bun(bun_data['name'], bun_data['price'])
        assert bun.get_price() == bun_data['price']