import pytest
from praktikum.bun import Bun


class TestBun:
    """Тесты для класса Bun."""

    def test_get_name_valid_name_returns_name(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_name() == "black bun"

    def test_get_name_empty_name_returns_empty_string(self):
        bun = Bun("", 100.0)
        assert bun.get_name() == ""

    def test_get_price_valid_price_returns_price(self):
        bun = Bun("black bun", 100.0)
        assert bun.get_price() == 100.0

    def test_get_price_zero_price_returns_zero(self):
        bun = Bun("black bun", 0.0)
        assert bun.get_price() == 0.0

    def test_get_price_float_price_returns_price(self):
        bun = Bun("black bun", 99.99)
        assert bun.get_price() == pytest.approx(99.99)

    def test_init_valid_name_and_price_stores_values(self):
        bun = Bun("black bun", 100.0)
        assert bun.name == "black bun" and bun.price == 100.0

    def test_init_two_buns_different_values_are_independent(self):
        bun1 = Bun("bun1", 100.0)
        bun2 = Bun("bun2", 200.0)
        assert bun1.get_name() != bun2.get_name() and bun1.get_price() != bun2.get_price()
        