import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import *


class TestBurger:
    def test_set_buns_true(self, burger):
        mock_bun = Mock()
        mock_bun.name = 'mega bun'
        mock_bun.price = 700

        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    def test_add_ingredient_two_ingredient_added(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = "mex sauce"
        mock_ingredient.price = 323

        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        assert len(burger.ingredients) == 2

    def test_remove_ingredient_removed(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = "mex sauce"
        mock_ingredient.price = 323

        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

    def test_move_ingredient_moved(self, burger):
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = "mex sauce"
        mock_ingredient.price = 323
        burger.add_ingredient(mock_ingredient)

        mock_second_ingredient = Mock()
        mock_second_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_second_ingredient.name = "crocodile"
        mock_second_ingredient.price = 200
        burger.add_ingredient(mock_second_ingredient)
        burger.move_ingredient(0, 1)
        assert burger.ingredients[0] == mock_second_ingredient

    @pytest.mark.parametrize('bun_price, ingredient_price, burger_price', [[99, 55, 253],
                                                                           [0, 17, 17],
                                                                           [14, 0, 28],
                                                                           [0, 0, 0]])
    def test_get_price_true(self, burger, bun_price, ingredient_price, burger_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        burger.add_ingredient(mock_ingredient)
        assert burger.get_price() == burger_price

    @pytest.mark.parametrize('bun_price, bun_name, ingredient_price, ingredient_type, ingredient_name, burger_price',
                             [[99, 'crazy bun', 55, INGREDIENT_TYPE_SAUCE.lower(), 'mex sauce', 253],
                              [14, 'amazing bun', 104, INGREDIENT_TYPE_FILLING.lower(), 'amazing sauce', 132]])
    def test_get_receipt_true(self, burger, bun_price, bun_name, ingredient_price,
                              ingredient_type, ingredient_name, burger_price):
        mock_bun = Mock()
        mock_bun.get_price.return_value = bun_price
        mock_bun.get_name.return_value = bun_name
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = ingredient_price
        mock_ingredient.get_type.return_value = ingredient_type
        mock_ingredient.get_name.return_value = ingredient_name
        burger.add_ingredient(mock_ingredient)

        receipt_example = (f'(==== {bun_name} ====)\n= {ingredient_type} {ingredient_name} =\n(==== {bun_name} ====)'
                           f'\n\nPrice: {burger_price}')

        assert receipt_example == burger.get_receipt()
