from unittest.mock import patch

import pytest

import data
from praktikum import ingredient_types
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns_bun_set_successfully(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun.name == data.BUN_NAME

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_add_ingredient_added_successfully(self, mock_ingredient, ingredient_type):
        mock_ingredient.get_name.return_value = 'ингредиент'
        mock_ingredient.get_price.return_value = 100
        mock_ingredient.get_type.return_value = ingredient_type
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    def test_remove_ingredient_removed_successfully(self):
        burger = Burger()
        burger.ingredients = data.LIST_INGREDIENTS
        removed_ingredient = data.LIST_INGREDIENTS[0]
        burger.remove_ingredient(0)
        assert removed_ingredient not in burger.ingredients

    def test_move_ingredient_moved_successfully(self):
        burger = Burger()
        burger.ingredients = data.LIST_INGREDIENTS
        moved_ingredient = data.LIST_INGREDIENTS[0]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == moved_ingredient

    def test_get_price_burger_bun_and_sauce_price_got_correct(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        expected_price = mock_bun.price * 2 + mock_ingredient.price
        assert burger.get_price() == expected_price

    @patch('praktikum.burger.Burger.get_price', return_value=2600)
    def test_get_receipt_got_successfully(self, mock_get_price, mock_bun, mock_ingredient):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        burger.get_price()
        receipt = burger.get_receipt()
        assert (receipt == f'(==== Краторная булка N-200i ====)\n= sauce Соус Spicy-X =\n(==== Краторная булка N-200i '
                           f'====)\n\nPrice: 2600')
