from models.bun import Bun
from utils.constants import BUN_BURGER, PRICE_BUN

class TestBun:
    """Тесты для класса Bun"""

    def test_bun_init(self):
        """Проверяем, что конструктор инициализирует поля name и price корректно через методы доступа"""
        bun = Bun(BUN_BURGER, PRICE_BUN)
        assert bun.get_name() == BUN_BURGER
        assert bun.get_price() == PRICE_BUN

    def test_bun_get_name(self):
        """Проверяем, что метод get_name() возвращает ожидаемое значение"""
        bun = Bun(BUN_BURGER, PRICE_BUN)
        assert bun.get_name() == BUN_BURGER

    def test_bun_get_price(self):
        """Проверяем, что метод get_price() возвращает ожидаемое значение"""
        bun = Bun(BUN_BURGER, PRICE_BUN)
        assert bun.get_price() == PRICE_BUN