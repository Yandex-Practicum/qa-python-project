import pytest
from praktikum.bun import Bun


class TestBun:
    # Тесты для get_name()
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 300.0),
    ])
    def test_bun_get_name_returns_correct_name(self, name, price):
        bun = Bun(name, price)
        assert bun.get_name() == name

    # Тесты для get_price()
    @pytest.mark.parametrize("name, price", [
        ("black bun", 100),
        ("white bun", 200.5),
        ("red bun", 300.0),
    ])
    def test_bun_get_price_returns_correct_price(self, name, price):
        bun = Bun(name, price)
        assert bun.get_price() == price
        