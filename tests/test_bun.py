import pytest
from praktikum.bun import Bun

def test_bun_initialization(bun_data):
    """Тестируем инициализацию объекта Bun"""
    for bun in bun_data:
        assert isinstance(bun, Bun)
        assert bun.get_name() in ["black bun", "white bun", "red bun"]
        assert bun.get_price() in [100, 200, 300]

@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300)
])
def test_bun_properties(bun_data, name, price):
    """Тестируем свойства булочек"""
    bun = next((b for b in bun_data if b.get_name() == name), None)
    assert bun is not None
    assert bun.get_name() == name
    assert bun.get_price() == price

def test_bun_get_name(bun_data):
    """Тестируем метод get_name"""
    for bun in bun_data:
        assert bun.get_name() == bun.name, "Метод get_name возвращает неправильное имя булочки"

def test_bun_get_price(bun_data):
    """Тестируем метод get_price"""
    for bun in bun_data:
        assert bun.get_price() == bun.price, "Метод get_price возвращает неправильную цену булочки"
