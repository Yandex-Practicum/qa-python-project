import pytest

from data import Data
from praktikum.bun import Bun


class TestBun:

    bun_data = [
        (Data.BUN_1, Data.BUN_1_PRICE),
        (Data.BUN_2, Data.BUN_2_PRICE),
        (Data.BUN_3, Data.BUN_3_PRICE)
    ]

    # проверка, что get_name возвращает название булки
    @pytest.mark.parametrize('name, price', bun_data)
    def test_get_name_returns_bun_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    # проверка, что get_price возвращает цену булки
    @pytest.mark.parametrize('name, price', bun_data)
    def test_get_price_returns_bun_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
