import pytest
from Diplom_1.praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("white bun", 200),
    ("red bun", 300),
])
def test_bun_init(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price


@pytest.mark.parametrize("name", [
    ("black bun"),
    ("white bun"),
    ("red bun"),
])
def test_bun_get_name(name):
    bun = Bun(name, 100)
    assert bun.get_name() == name


@pytest.mark.parametrize("price", [
    (100),
    (200),
    (300),
])
def test_bun_get_price(price):
    bun = Bun("bun", price)
    assert bun.get_price() == price



