import pytest
from praktikum.bun import Bun
from data import BUN_TEST_DATA


@pytest.mark.parametrize("name, price", BUN_TEST_DATA)
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
