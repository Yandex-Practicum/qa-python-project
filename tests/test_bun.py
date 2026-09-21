import pytest
from praktikum.bun import Bun


class TestBun:

    @pytest.mark.parametrize(
        'name, price',
        [
            ('black bun', 100),
            ('white bun', 200.5),
            ('red bun', 0),
            ('космическая булочка', 999.99),
            ('!@#$%', 50.0),
        ]
    )
    def test_bun_initialization_and_getters(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize(
        'name, price',
        [
            ('fluffy bun', 150),
            ('sesame bun', 0.01),
        ]
    )
    def test_bun_get_name_returns_correct_name(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_name() == name

    @pytest.mark.parametrize(
        'name, price',
        [
            ('sweet bun', 300),
            ('rye bun', 250.75),
        ]
    )
    def test_bun_get_price_returns_correct_price(self, name, price):
        bun = Bun(name=name, price=price)
        assert bun.get_price() == price
