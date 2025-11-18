from praktikum.bun import Bun
from data import BunData
import pytest


class TestBun:
    # Проверяет, что метод get_name возвращает корректное название булочки
    def test_get_name_bun_success(self):
        bun = Bun(BunData.bun_name, BunData.bun_price_int)
        assert bun.get_name() == BunData.bun_name

    # Проверяет, что метод get_price возвращает корректную цену булочки для целочисленных и дробных значений
    @pytest.mark.parametrize('price', [BunData.bun_price_int, BunData.bun_price_float])
    def test_get_price_bun_success(self, price):
        bun = Bun(BunData.bun_name, price)
        assert bun.get_price() == price