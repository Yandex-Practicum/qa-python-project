from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestBurger:

    def test_new_burger_has_no_ingredients(self, burger):
        assert burger.ingredients == []

    def test_set_buns_sets_bun(self, burger, mock_bun):
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient_adds_to_end(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        assert burger.ingredients == [mock_sauce, mock_filling]

    def test_remove_ingredient_removes_by_index(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.remove_ingredient(0)

        assert burger.ingredients == [mock_filling]

    def test_move_ingredient_changes_position(self, burger, mock_sauce, mock_filling):
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_filling, mock_sauce]

    @pytest.mark.parametrize(
        'bun_price, ingredient_prices, expected_price',
        [
            (100, [], 200),
            (100, [50], 250),
            (200, [100, 300], 800)
        ]
    )
    def test_get_price_returns_buns_and_ingredients_sum(self, burger, bun_price, ingredient_prices, expected_price):
        bun = Mock(spec=Bun)
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
        for price in ingredient_prices:
            ingredient = Mock(spec=Ingredient)
            ingredient.get_price.return_value = price
            burger.add_ingredient(ingredient)

        assert burger.get_price() == expected_price

    def test_get_receipt_returns_burger_info(self, burger, mock_bun, mock_sauce, mock_filling):
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        expected_receipt = (
            '(==== black bun ====)\n'
            '= sauce hot sauce =\n'
            '= filling cutlet =\n'
            '(==== black bun ====)\n'
            '\n'
            'Price: 500'
        )

        assert burger.get_receipt() == expected_receipt
