import pytest
from bun import Bun

def test_bun_creation():
    bun = Bun("white bun", 200)
    assert bun.get_name() == "white bun"
    assert bun.get_price() == 200

@pytest.mark.parametrize("name, price", [
    ("black bun", 100),
    ("red bun", 300),
])
def test_bun_parametrized(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
