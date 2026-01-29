import pytest
from praktikum.bun import Bun

class TestBun:

    @pytest.mark.parametrize("name, expected_name", [
        ("Булка Интерстеллар", "Булка Интерстеллар"),
        ("Булка Инт3рст3ллар", "Булка Инт3рст3ллар"),
        ("Бесплатная Марсианская Булочка", "Бесплатная Марсианская Булочка"),
    ])
    def test_bun_get_name(self, name, expected_name):
        bun = Bun(name, 5)
        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("price, expected_price", [
        (3, 3),
        (5.59, 5.59),
        (0.0, 0.0),
    ])
    def test_bun_get_price(self, price, expected_price):
        bun = Bun("Межгалактическая Булочка", price)
        assert bun.get_price() == expected_price

