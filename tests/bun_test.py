import pytest

from praktikum.bun import Bun
from tests.test_data import BUN_NAME, BUN_PRICE


class TestBunGetName:
    """Тесты метода get_name."""

    @pytest.mark.parametrize(
        "name",
        [
            "black bun",
            "white bun",
            "red bun",
            "",
            "булка с длинным названием",
        ],
    )
    def test_get_name_returns_name(self, name):
        bun = Bun(name, BUN_PRICE)
        assert bun.get_name() == name


class TestBunGetPrice:
    """Тесты метода get_price."""

    @pytest.mark.parametrize(
        "price",
        [
            0.0,
            100.0,
            300.0,
            9999.99,
        ],
    )
    def test_get_price_returns_price(self, price):
        bun = Bun(BUN_NAME, price)
        assert bun.get_price() == price