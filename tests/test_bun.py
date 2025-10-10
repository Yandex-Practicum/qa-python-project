import pytest
from data.bun_data import params_name, params_price
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("actual_name, expected_name", params_name)
    def test_get_name(self, actual_name, expected_name):
        bun = Bun(actual_name, 100.5)
        assert bun.get_name() == expected_name and isinstance(bun.get_name(), str)

    @pytest.mark.parametrize("actual_price, expected_price", params_price)
    def test_get_price(self, actual_price, expected_price):
        bun = Bun("Name", actual_price)
        assert bun.get_price() == pytest.approx(expected_price) and isinstance(bun.get_price(), float)
