import pytest
from unittest.mock import MagicMock

from praktikum.burger import Burger


class TestBurgerPrice:
    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (0, [], 0),
            (50, [], 100),
            (80, [20], 180),
            (100, [10, 20, 30], 260),
        ],
    )
    def test_total_price_parametrized(self, bun_price, ingredient_prices, expected):
        burger = Burger()
        bun = MagicMock()
        bun.get_price.return_value = bun_price
        bun.get_name.return_value = "Any Bun"
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = MagicMock()
            ingredient.get_price.return_value = price
            ingredient.get_name.return_value = f"i{price}"
            ingredient.get_type.return_value = "FILLING"
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected
