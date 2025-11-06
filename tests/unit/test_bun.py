import pytest
from bun import Bun

@pytest.mark.parametrize("name, price", [
    ("black bun", 100.0),
    ("white bun", 200.0),
    ("sesame bun", 250.0)
])
def test_bun_basic(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price