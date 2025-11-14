import pytest
from praktikum.bun import Bun

@pytest.mark.parametrize(
    "name, price", [
        ("Classic", 150),
        ("Sesame", 200),
        ("Gluten-Free", 250)
    ]
)
def test_bun_initialization(name, price):
    bun = Bun(name, price)
    assert bun.name == name
    assert bun.price == price

def test_bun_get_name():
    bun = Bun("Classic", 1.5)
    assert bun.get_name() == "Classic"

def test_bun_get_price():
    bun = Bun("Classic", 1.5)
    assert bun.get_price() == 1.5