import pytest
from praktikum.bun import Bun


class TestBun:
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988)
    ])
    def test_bun_get_name(self, name, price):
        """Проверяем, что метод get_name возвращает правильное название булочки."""
        bun = Bun(name, price)
        assert bun.get_name() == name
    
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200),
        ("red bun", 300),
        ("Краторная булка N-200i", 1255),
        ("Флюоресцентная булка R2-D3", 988)
    ])
    def test_bun_get_price(self, name, price):
        """Проверяем, что метод get_price возвращает правильную цену булочки."""
        bun = Bun(name, price)
        assert bun.get_price() == price
    
    def test_bun_creation_with_float_price(self):
        """Проверяем создание булочки с дробной ценой."""
        bun = Bun("test bun", 99.99)
        assert bun.get_price() == 99.99