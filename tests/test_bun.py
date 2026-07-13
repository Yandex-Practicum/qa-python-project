import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize(
    "name, price",
    [
        ("white bun", 200),
        ("black bun", 100),
        ("red bun", 300)
    ]
)
def test_bun_fields(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
    