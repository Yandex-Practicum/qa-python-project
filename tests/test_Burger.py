from unittest.mock import Mock, patch

import pytest

import data


class TestBurger:

    def test_set_buns(self, burger, bun):
        mock_bun = Mock()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)

        assert len(burger.ingredients) == 1

    def test_remove_ingredient(self, burger):
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 0

    def test_move_ingredient(self, burger):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0,1)

        assert burger.ingredients[1] == mock_ingredient_1

    @pytest.mark.parametrize(
        'price_bun, price_ingredient, result_price',
        [
            [100.0, 100.0, 300.0],
            [0.0, 0.0, 0.0],
            [500.0, 30000.0, 31000.0]
        ]
    )
    def test_get_price(self, price_bun, price_ingredient, result_price, mock_bun, mock_ingredient, burger):
        mock_bun.get_price.return_value = price_bun
        mock_ingredient.get_price.return_value = price_ingredient
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        assert burger.get_price() == result_price

    @patch('praktikum.bun.Bun.get_name', return_value=data.NAME_BUN)
    @patch('praktikum.ingredient.Ingredient.get_name', return_value=data.NAME_INGREDIENT)
    def test_get_receipt(self, mock_ingredient_name, mock_bun_name, bun, ingredient, burger):
        burger.set_buns(bun)
        burger.add_ingredient(ingredient)

        assert data.NAME_BUN and data.NAME_INGREDIENT in burger.get_receipt()

