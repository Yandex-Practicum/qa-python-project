import pytest

import DATA
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", DATA.Buns.BUNS)
def test_bun_initialization_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", DATA.Buns.BUNS)
def test_bun_initialization_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price
