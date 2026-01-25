import pytest
from data import BUN_NAME_1, BUN_NAME_2, BUN_PRICE
from praktikum.bun import Bun


class TestBun:
    @pytest.mark.parametrize("name", [BUN_NAME_1, BUN_NAME_2])
    def test_bun_name(self, name):
        bun = Bun(name, BUN_PRICE)
        assert bun.get_name() == name

    def test_bun_price(self):
        bun = Bun(BUN_NAME_1, BUN_PRICE)
        assert bun.get_price() == BUN_PRICE
