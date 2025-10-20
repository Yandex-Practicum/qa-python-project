import pytest

from praktikum.bun import Bun


@pytest.mark.parametrize(
    "name, price",
    [
        ("black bun", 100.0),
        ("white bun", 0.0),
        ("sesame bun", 199.99),
    ],
)
class TestBun:
    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price

