import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name, price', [
        ["black bun", 88.25],
        ["white bun", -100.78],
        ["black bun", 0]
    ])
class TestBun:

    def test_get_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    def test_get_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
