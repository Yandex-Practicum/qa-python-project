import pytest
from praktikum.bun import Bun

class TestBun:
    def test_bun_initialization(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"
        assert bun.get_price() == 100.0

    @pytest.mark.parametrize("name,price", [
        ("Black bun", 100.0),
        ("White bun", 200.0),
        ("Red bun", 250.5),
    ])
    def test_bun_getters_with_different_values(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    def test_bun_price_is_float(self):
        """Проверка, что цена корректно возвращается как float при инициализации float значением"""
        bun = Bun("Test bun", 100.0)
        assert isinstance(bun.get_price(), float)
        assert bun.get_price() == 100.0

    def test_bun_price_with_int_input(self):
        """Проверка, что при передаче целого числа (int) цена корректно сохраняется и доступна"""
        bun = Bun("Test bun 2", 200)
        # Проверяем конечное состояние объекта — значение цены
        assert bun.get_price() == 200
