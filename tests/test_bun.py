import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [("black bun", 30), ("white bun", 50)])
def test_bun_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", [("black bun", 30), ("white bun", 50)])
def test_bun_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
