from unittest.mock import Mock
from unittest.mock import patch
import pytest
from praktikum import ingredient_types
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


class TestBurger:
    def test_set_buns_bun_added_successfully(self):
        mock_bun = Mock()
        mock_bun.bun = Bun("булочка с кунжутом", 100)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        actual_result = burger.bun.get_name()
        assert actual_result == "булочка с кунжутом"

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'garlic', 8.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25]
    ])
    def test_add_ingredient_ingredient_added_successfully(self, ingredient_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredient)
        assert len(burger.ingredients) == 1

    @pytest.mark.parametrize('ingredient_type, name, price', [
        [ingredient_types.INGREDIENT_TYPE_SAUCE, 'cheese', 6.5],
        [ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5]
    ])
    def test_remove_ingredient_ingredient_removed_successfully(self, ingredient_type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.ingredient = Ingredient(ingredient_type, name, price)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_move_ingredient_ingredient_move_successfully(self):
        mock_ingredient = Mock()
        mock_ingredient.ingredient_1 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 12.5)
        mock_ingredient.ingredient_2 = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'bacon', 25)
        burger = Burger()
        burger.add_ingredient(mock_ingredient.ingredient_1)
        burger.add_ingredient(mock_ingredient.ingredient_2)
        burger.move_ingredient(1, 0)
        assert burger.ingredients.index(mock_ingredient.ingredient_2) == 0

    @patch('praktikum.bun.Bun.get_price', return_value=100)
    @patch('praktikum.ingredient.Ingredient.get_price', return_value=12.5)
    def test_get_price_returned_correct_price_burger(self, mock_bun_get_price, mock_ingredient_get_price):
        mock_bun = Mock()
        mock_bun.bun = Bun("булочка с кунжутом", 999)
        burger = Burger()
        burger.set_buns(mock_bun.bun)
        mock_ingredient = Mock()
        mock_ingredient.ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pickles', 999)
        burger.add_ingredient(mock_ingredient.ingredient)
        actual_result = burger.get_price()
        assert actual_result == 212.5

    @patch('praktikum.bun.Bun.get_name', return_value="булочка с кунжутом")
    @patch('praktikum.ingredient.Ingredient.get_type', return_value='FILLING')
    @patch('praktikum.ingredient.Ingredient.get_name', return_value='pickles')
    def test_get_receipt_returned_correct_receipt_burger(self, mock_bun_get_name, mock_ingredient_get_type, mock_ingredient_get_name):
        burger = Burger()
        mock_bun = Mock()
        mock_bun.bun = Bun("булочка", 100)
        burger.set_buns(mock_bun.bun)
        mock_ingredient = Mock()
        mock_ingredient.ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, 'pic', 12.5)
        burger.add_ingredient(mock_ingredient.ingredient)
        actual_result = burger.get_receipt()
        assert actual_result == '(==== булочка с кунжутом ====)\n''= filling pickles =\n''(==== булочка с кунжутом ====)\n''\n''Price: 212.5'





