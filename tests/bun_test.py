import pytest
from praktikum.bun import Bun
from data import BUN_TEST_DATA


@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price


@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
