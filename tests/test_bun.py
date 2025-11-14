import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize("name, price", [
    ("Булочка", 0.70),
    ("Маковый штрудель", 120.99),
    ("77", 0),
    ("", 10.0)
])
def test_bun_creation(name, price):
    bun = Bun(name, price)
    assert bun.get_name() == name
    assert bun.get_price() == price

