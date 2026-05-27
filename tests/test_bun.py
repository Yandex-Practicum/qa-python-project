import pytest

from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5)
    ])
    def test_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5)
    ])
    def test_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price