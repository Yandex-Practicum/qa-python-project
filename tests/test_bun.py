import pytest
from praktikum.bun import Bun

BUN_NAME_1 = "sesame"
BUN_NAME_2 = "plain"
BUN_PRICE = 50.0

@pytest.mark.parametrize("name", [BUN_NAME_1, BUN_NAME_2])
def test_bun_name(name):
    bun = Bun(name, BUN_PRICE)
    assert bun.get_name() == name

def test_bun_price():
    bun = Bun(BUN_NAME_1, BUN_PRICE)
    assert bun.get_price() == BUN_PRICE