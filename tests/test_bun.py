import pytest
from praktikum.bun import Bun

# Тесты на класс Bun
class TestBun:
    # Проверка корректного сохранения названия булки
    @pytest.mark.parametrize("name, price",[("черная булка", 150), ("белая булка", 200)],)
    def test_bun_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Проверка корректного сохранения цены булки
    @pytest.mark.parametrize("name, price",[("черная булка", 150), ("белая булка", 200)],)
    def test_bun_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price


