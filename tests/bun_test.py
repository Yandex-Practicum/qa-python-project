import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun"""

    def test_create_bun_with_valid_data(self):
        """Тест создания булочки с валидными данными"""
        bun = Bun("White Bun", 2.5)
        assert bun.get_name() == "White Bun"
        assert bun.get_price() == 2.5

    def test_get_name_returns_correct_name(self):
        """Тест проверки метода get_name"""
        bun = Bun("Black Bun", 3.0)
        assert bun.get_name() == "Black Bun"

    def test_get_price_returns_correct_price(self):
        """Тест проверки метода get_price"""
        bun = Bun("Sesame Bun", 1.75)
        assert bun.get_price() == 1.75

    def test_bun_with_zero_price(self):
        """Тест создания булочки с нулевой ценой"""
        bun = Bun("Free Bun", 0.0)
        assert bun.get_name() == "Free Bun"
        assert bun.get_price() == 0.0

    def test_bun_with_empty_name(self):
        """Тест создания булочки с пустым названием"""
        bun = Bun("", 1.0)
        assert bun.get_name() == ""
        assert bun.get_price() == 1.0

    def test_bun_with_special_characters_in_name(self):
        """Тест создания булочки со специальными символами в названии"""
        bun = Bun("Bun #1 (Premium)", 5.99)
        assert bun.get_name() == "Bun #1 (Premium)"
        assert bun.get_price() == 5.99

    def test_bun_with_negative_price(self):
        """Тест создания булочки с отрицательной ценой"""
        bun = Bun("Discount Bun", -1.5)
        assert bun.get_name() == "Discount Bun"
        assert bun.get_price() == -1.5