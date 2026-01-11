from praktikum.bun import Bun
from data import TestData
import pytest


class TestBun:

    @pytest.mark.parametrize('bun_name',
                             [TestData.BUN_NAME_VALID_BLACK, TestData.BUN_NAME_VALID_WHITE, TestData.BUN_NAME_VALID_RED])
    def test_get_name_successful(self, bun_name):
        bun = Bun(bun_name, TestData.BUN_PRICE_VALID)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize('bun_name',
                             [TestData.BUN_NAME_WITH_SYMBOLS, TestData.BUN_NAME_EMPTY])
    def test_get_name_unsuccessful(self, bun_name):
        bun = Bun(bun_name, TestData.BUN_PRICE_VALID)
        assert bun.get_name() != bun_name

    def test_get_price_unsuccessful(self):
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, TestData.BUN_PRICE_LESS_THAN_ZERO)
        assert bun.get_price() != TestData.BUN_PRICE_LESS_THAN_ZERO

    @pytest.mark.parametrize('bun_price',
                             [TestData.BUN_PRICE_VALID, TestData.BUN_PRICE_FLOAT])
    def test_get_price_successful(self, bun_price):
        bun = Bun(TestData.BUN_NAME_VALID_WHITE, bun_price)
        assert bun.get_price() == bun_price
