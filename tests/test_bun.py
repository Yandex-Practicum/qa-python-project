import pytest
from bun import Bun


def test_bun_has_name():
    bun = Bun(name="black bun", price=100)
    assert bun.name == "black bun"


def test_bun_has_price():
    bun = Bun(name="black bun", price=100)
    assert bun.price == 100


@pytest.mark.parametrize(
    "name, price",
    [
        ("white bun", 50),
        ("black bun", 100),
        ("alien bun", 999),
    ]
)
def test_bun_parametrized(name, price):
    bun = Bun(name=name, price=price)
    assert bun.name == name
    assert bun.price == price
