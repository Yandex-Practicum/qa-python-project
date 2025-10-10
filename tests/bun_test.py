import pytest

from praktikum.bun import Bun
from data.test_data import BUN_NAME, BUN_PRICE, BUN_NAME_2, BUN_PRICE_2


class TestBun:
    """Тесты для класса Bun"""

    def test_bun_creation(self):
        """Тест создания объекта булочки"""
        bun = Bun(BUN_NAME, BUN_PRICE)
        
        assert bun.name == BUN_NAME
        assert bun.price == BUN_PRICE

    def test_get_name(self):
        """Тест метода get_name"""
        bun = Bun(BUN_NAME, BUN_PRICE)
        
        result = bun.get_name()
        
        assert result == BUN_NAME

    def test_get_price(self):
        """Тест метода get_price"""
        bun = Bun(BUN_PRICE, BUN_PRICE)
        
        result = bun.get_price()
        
        assert result == BUN_PRICE

    def test_bun_with_different_values(self):
        """Тест создания булочки с другими значениями"""
        bun = Bun(BUN_NAME_2, BUN_PRICE_2)
        
        assert bun.get_name() == BUN_NAME_2
        assert bun.get_price() == BUN_PRICE_2

    def test_bun_with_fixture(self, bun):
        assert bun.get_name() == BUN_NAME
        assert bun.get_price() == BUN_PRICE 