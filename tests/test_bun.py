import pytest

from praktikum.bun import Bun
from tests.data import BUN_CASES


class TestBun:
    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_name_returns_given_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", BUN_CASES)
    def test_get_price_returns_given_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
