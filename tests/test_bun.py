import pytest
from praktikum.bun import Bun
from data_tests import bun_names, bun_prices


class TestBun:
    @pytest.mark.parametrize("name, expected_name", bun_names)
    def test_get_name_with_correct_data(self, name, expected_name):
        bun = Bun(name=name, price=5.0)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("price, expected_price", bun_prices)
    def test_get_price_with_correct_data(self, price, expected_price):
        bun = Bun(name="Ramon", price=price)
        assert bun.get_price() == expected_price