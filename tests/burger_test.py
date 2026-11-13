from unittest.mock import MagicMock

import pytest

from praktikum.burger import Burger


class TestBurger:
    """Юнит-тесты для класса Burger."""

    def test_init_burger_without_bun_and_ingredients(self):
        burger = Burger()

        assert burger.bun is None
        assert burger.ingredients == []

    def test_set_buns(self):
        burger = Burger()
        bun = MagicMock()

        burger.set_buns(bun)

        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        ingredient = MagicMock()

        burger.add_ingredient(ingredient)

        assert len(burger.ingredients) == 1
        assert burger.ingredients[0] == ingredient

    def test_remove_ingredient(self):
        burger = Burger()
        first = MagicMock()
        second = MagicMock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)

        burger.remove_ingredient(0)

        assert burger.ingredients == [second]

    def test_move_ingredient(self):
        burger = Burger()
        first = MagicMock()
        second = MagicMock()
        third = MagicMock()
        burger.add_ingredient(first)
        burger.add_ingredient(second)
        burger.add_ingredient(third)

        burger.move_ingredient(0, 2)

        assert burger.ingredients == [second, third, first]

    @pytest.mark.parametrize(
        'bun_price, ingredient_prices, expected',
        [
            (100, [], 200),
            (50, [10], 110),
            (200, [50, 30, 20], 500),
            (12.5, [3.2, 7.8], 36.0),
        ],
    )
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()

        bun = MagicMock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)

        for price in ingredient_prices:
            ingredient = MagicMock()
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected

    def test_get_receipt(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = 'black bun'
        bun.get_price.return_value = 100
        burger.set_buns(bun)

        sauce = MagicMock()
        sauce.get_type.return_value = 'sauce'
        sauce.get_name.return_value = 'hot sauce'
        sauce.get_price.return_value = 50
        burger.add_ingredient(sauce)

        filling = MagicMock()
        filling.get_type.return_value = 'filling'
        filling.get_name.return_value = 'cutlet'
        filling.get_price.return_value = 25
        burger.add_ingredient(filling)

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 275'
        )

        assert burger.get_receipt() == expected_receipt

    def test_get_receipt_empty_burger(self):
        burger = Burger()

        bun = MagicMock()
        bun.get_name.return_value = 'white bun'
        bun.get_price.return_value = 200
        burger.set_buns(bun)

        expected_receipt = (
            '(==== white bun ====)\n'
            '(==== white bun ====)\n'
            '\n'
            'Price: 400'
        )

        assert burger.get_receipt() == expected_receipt
