import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 80),
        ("sesame bun", 120),
    ]
)
def test_bun_constructor(name, price):
    bun = Bun(name, price)

    assert bun.name == name
    assert bun.price == price


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 80),
    ]
)
def test_get_name(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 80),
    ]
)
def test_get_price(name, price):
    bun = Bun(name, price)

    assert bun.get_price() == price
