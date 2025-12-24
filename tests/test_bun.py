import pytest
from praktikum.bun import Bun
from data import bun_cases

class TestBun:
    @pytest.mark.parametrize("bun_name, bun_price", bun_cases)
    def test_bun_name_returns_expected(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_name() == bun_name

    @pytest.mark.parametrize("bun_name, bun_price", bun_cases)
    def test_bun_price_returns_expected(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.get_price() == bun_price

    @pytest.mark.parametrize("bun_name, bun_price", bun_cases)
    def test_bun_fields_match_constructor_values(self, bun_name, bun_price):
        bun = Bun(bun_name, bun_price)
        assert bun.name == bun_name
        assert bun.price == bun_price
