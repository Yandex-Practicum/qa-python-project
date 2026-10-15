import pytest

from bun import Bun
from tests.test_data import BUN_NAME, BUN_PRICE


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [(BUN_NAME, BUN_PRICE), ("white bun", 200)],
    )
    def test_get_name_returns_bun_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [(BUN_NAME, BUN_PRICE), ("white bun", 200)],
    )
    def test_get_price_returns_bun_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
