import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("Флюоресцентная булка", 988),
    ("Краторная булка", 1255)
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price
