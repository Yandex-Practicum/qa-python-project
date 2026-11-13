import pytest

from praktikum.bun import Bun


class TestBun:
    """Юнит-тесты для класса Bun."""

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('white bun', 200),
        ('red bun', 300),
        ('gluten free bun', 150.5),
    ])
    def test_bun_init(self, name, price):
        bun = Bun(name, price)

        assert bun.name == name
        assert bun.price == price

    @pytest.mark.parametrize('name, price', [
        ('black bun', 100),
        ('red bun', 300.75),
    ])
    def test_get_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize('price', [0, 100, 250.5, 1000])
    def test_get_price(self, price):
        bun = Bun('bun', price)

        assert bun.get_price() == price
