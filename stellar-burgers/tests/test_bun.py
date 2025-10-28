import pytest
from praktikum.bun import Bun
from data import (
    WHITE_BUN_NAME, WHITE_BUN_PRICE,
    RED_BUN_NAME, RED_BUN_PRICE,
    BLACK_BUN_NAME, BLACK_BUN_PRICE,
    BUN_VARIANTS
)


class TestBun:
    """Тестовый класс для булочки."""

    def test_bun_creation_sets_name_and_price(self):
        """Тест создания булочки с установкой имени и цены."""
        bun = Bun(WHITE_BUN_NAME, WHITE_BUN_PRICE)
        assert bun.name == WHITE_BUN_NAME
        assert bun.price == WHITE_BUN_PRICE

    def test_get_name_returns_correct_value(self):
        """Тест метода get_name возвращает корректное имя."""
        bun = Bun(RED_BUN_NAME, RED_BUN_PRICE)
        assert bun.get_name() == RED_BUN_NAME

    def test_get_price_returns_correct_value(self):
        """Тест метода get_price возвращает корректную цену."""
        bun = Bun(BLACK_BUN_NAME, BLACK_BUN_PRICE)
        assert bun.get_price() == BLACK_BUN_PRICE

    @pytest.mark.parametrize('name, price', [
        ("white", 100),
        ("black", 120),
        ("sesame", 150),
    ])
    def test_bun_with_different_prices_and_names(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price
