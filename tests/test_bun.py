import pytest

from bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("white bun", 200),
    ],
)
def test_bun_initialization_sets_attributes(name, price):
    bun = Bun(name, price)

    assert bun.name == name
    assert bun.price == price


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100),
        ("red bun", 300),
    ],
)
def test_get_name_returns_name(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    "price",
    [100, 150.5, 300],
)
def test_get_price_returns_price(price):
    bun = Bun("test bun", price)

    assert bun.get_price() == price
