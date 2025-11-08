import pytest

from src.bun import Bun


@pytest.mark.parametrize("name,price", [
    ("White", 0),
    (" Sesame ", 2.99),
    ("Ржаная", 10.0),
])
def test_bun_valid(name, price):
    b = Bun(name=name, price=price)
    assert b.get_name() == name
    assert b.get_price() == price
