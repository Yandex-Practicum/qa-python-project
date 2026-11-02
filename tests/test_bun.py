import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("краторная булка", 1255),
        ("флюоресцентная булка", 988),
    ],
)
def test_bun_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize(
    "name, price",
    [
        ("краторная булка", 1255),
        ("флюоресцентная булка", 988),
    ],
)
def test_bun_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
