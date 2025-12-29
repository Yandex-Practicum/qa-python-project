import pytest
from bun import Bun


BUN_DATA = [
    ("black bun", 100),
    ("white bun", 200),
    ("gluten free", 300),
]

@pytest.mark.parametrize("name, price", BUN_DATA)
def test_bun_get_name(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name


@pytest.mark.parametrize("name, price", BUN_DATA)
def test_bun_get_price(name, price):
    bun = Bun(name, price)
    assert bun.get_price() == price