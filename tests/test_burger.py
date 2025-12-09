from praktikum.burger import Burger
from data import MockBun, MockIngredients
import data
from unittest.mock import patch


class TestBurger:
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self, mock_two_ingredients):
        burger = Burger()
        burger.ingredients = mock_two_ingredients
        burger.remove_ingredient(0)

        assert len(burger.ingredients) == 1

    def test_move_ingredient(self, mock_two_ingredients):
        burger = Burger()
        burger.ingredients = mock_two_ingredients.copy()
        burger.move_ingredient(1, 0)

        assert burger.ingredients[0] == mock_two_ingredients[1]

    def test_get_price(self, mock_bun, mock_two_ingredients):
        burger = Burger()
        mock_bun.get_price.return_value = MockBun.price
        mock_two_ingredients[0].get_price.return_value = MockIngredients.price
        mock_two_ingredients[1].get_price.return_value = MockIngredients.price_2
        burger.bun = mock_bun
        burger.ingredients = mock_two_ingredients
        actual_result = burger.get_price()

        assert actual_result == 100 * 2 + 100 + 200

    @patch('praktikum.burger.Burger.get_price', return_value=500)
    def test_get_receipt(self, mock_get_price, mock_bun, mock_two_ingredients):
        burger = Burger()
        mock_bun.get_name.return_value = MockBun.name
        mock_two_ingredients[0].get_name.return_value = MockIngredients.name
        mock_two_ingredients[0].get_type.return_value = MockIngredients.ingredient_type
        mock_two_ingredients[1].get_name.return_value = MockIngredients.name_2
        mock_two_ingredients[1].get_type.return_value = MockIngredients.ingredient_type_2
        burger.bun = mock_bun
        burger.ingredients = mock_two_ingredients
        actual_result = burger.get_receipt()

        assert actual_result == data.expected_receipt