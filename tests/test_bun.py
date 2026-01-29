import pytest
from ..bun import Bun
@pytest.mark.parametrize("name, price", [
    ("Лучшая", 9.9),
    ("Сырная", 1.3)
])
def test_configuration_bun(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

def test_get_name_bun():
    bun = Bun("Пышная", 1.1)
    assert bun.get_name() == "Пышная"

def test_get_price_bun():
    bun = Bun("Мягкая", 1.9)
    assert bun.get_price() == 1.9