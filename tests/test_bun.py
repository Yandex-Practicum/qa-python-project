import pytest
from data import Data
from praktikum.bun import Bun

@pytest.mark.parametrize("name, price", Data.BUNS)
def test_bun_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", Data.BUNS)
def test_bun_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price