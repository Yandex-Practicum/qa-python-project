import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    'name',
    [
        'black bun',
        'булочка',
        'bun-123',
        'bun!@#$',
    ],
)
def test_get_name_returns_init_value(name):
    bun = Bun(name, 100.0)

    assert bun.get_name() == name


@pytest.mark.parametrize(
    'price',
    [
        0,
        1,
        200.5,
        1_000_000.0,
        -10.5,
    ],
)
def test_get_price_returns_init_value(price):
    bun = Bun('black bun', price)

    assert bun.get_price() == price
