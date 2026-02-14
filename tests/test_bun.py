import pytest
from praktikum.bun import Bun
from tests.test_constants import (
    TEST_BUNS, BUN_TEST, PRICE_150
)


# Тесты для класса Bun.
class TestBun:

    @pytest.mark.parametrize("name,price", TEST_BUNS)
    def test_bun_get_name(self, name, price):
        # Проверка получения названия булочки.
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize("name,price", TEST_BUNS)
    def test_bun_get_price(self, name, price):
        # Проверка получения цены булочки.
        bun = Bun(name, price)
        assert bun.get_price() == price

    def test_bun_initialization(self):
        # Проверка инициализации булочки.
        bun = Bun(BUN_TEST, PRICE_150)
        assert bun.name == BUN_TEST
        assert bun.price == PRICE_150
