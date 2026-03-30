import pytest
from praktikum.bun import Bun


class TestBun:
    # Тестовые данные для проверки
    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
    ])
    def test_bun_get_name(self, name, price):
        """Проверяем, что get_name возвращает правильное название булки"""
        bun = Bun(name, price)
        assert bun.get_name() == name

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
    ])
    def test_bun_get_price(self, name, price):
        """Проверяем, что get_price возвращает правильную цену булки"""
        bun = Bun(name, price)
        assert bun.get_price() == price
