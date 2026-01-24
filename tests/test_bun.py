# tests/test_bun.py
import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 150),
    ("sesame bun", 120),
])  # Параметризация для проверки нескольких булочек
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
