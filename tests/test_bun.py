# Bun Class tests
from data import BUN
from conftest import test_bun, test_bun2
import pytest


class TestBun:

    def test_init_bun_name_matches_true(self, test_bun):
        assert isinstance(test_bun.name, str) and test_bun.name == BUN['name']

    @pytest.mark.parametrize('test_bun', [test_bun, test_bun2], indirect=True)  # check int and float price values
    def test_init_bun_price_matches_true(self, test_bun):
        assert isinstance(test_bun.price, (int, float)) and test_bun.price == BUN['price']

    def test_get_bun_name_true(self, test_bun):
        assert isinstance(test_bun.get_name(), str) and test_bun.get_name() == BUN['name']

    @pytest.mark.parametrize('test_bun', [test_bun, test_bun2], indirect=True)  # check int and float price values
    def test_get_bun_price_true(self, test_bun):
        assert isinstance(test_bun.get_price(), (int, float)) and test_bun.get_price() == BUN['price']
