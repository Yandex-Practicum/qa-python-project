import pytest

from praktikum.bun import Bun
from tests.constants import (
    BUN_BLACK_NAME,
    BUN_BLACK_PRICE,
    BUN_WHITE_NAME,
    BUN_WHITE_PRICE,
    BUN_RED_NAME,
    BUN_RED_PRICE,
)


class TestBun:
    @pytest.mark.parametrize(
        "name, price",
        [
            (BUN_BLACK_NAME, BUN_BLACK_PRICE),
            (BUN_WHITE_NAME, BUN_WHITE_PRICE),
            (BUN_RED_NAME, BUN_RED_PRICE),
            ("", 0),
            ("булочка с кунжутом", 99.99),
        ],
    )
    def test_bun_init(self, name, price):
        bun = Bun(name, price)
        assert (bun.name, bun.price) == (name, price)

    @pytest.mark.parametrize(
        "name, price",
        [
            (BUN_BLACK_NAME, BUN_BLACK_PRICE),
            (BUN_WHITE_NAME, BUN_WHITE_PRICE),
            (BUN_RED_NAME, BUN_RED_PRICE),
            ("", 0),
        ],
    )
    def test_get_name_returns_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        "name, price",
        [
            (BUN_BLACK_NAME, BUN_BLACK_PRICE),
            (BUN_WHITE_NAME, BUN_WHITE_PRICE),
            (BUN_RED_NAME, BUN_RED_PRICE),
            ("bun", 99.99),
        ],
    )
    def test_get_price_returns_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price