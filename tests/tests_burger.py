from unittest.mock import patch
import pytest
from data import DataBurger, DataBun, DataIngredient


# class for tests Burger methods
class TestsBurger:

    def test_set_buns(self, new_burger):
        new_burger.set_buns(DataBurger.BUN_DATA)
        assert new_burger.bun is not None

    @pytest.mark.parametrize(
        "ingredient",
        [
            DataBurger.INGREDIENT_DATA_FILLING,
            DataBurger.INGREDIENT_DATA_SAUCE
        ]
    )
    def test_add_ingredient(self, new_burger, ingredient):
        new_burger.add_ingredient(ingredient)
        assert new_burger.ingredients[0]["ingredient_type"] == ingredient["ingredient_type"]

    def test_remove_ingredient(self, new_burger):
        new_burger.ingredients = DataBurger.INGREDIENT_DATA_LIST
        new_burger.remove_ingredient(0)
        assert len(new_burger.ingredients) == 1

    def test_move_ingredient(self,new_burger):
        new_burger.ingredients = DataBurger.INGREDIENT_DATA_LIST
        new_burger.move_ingredient(0, 1)
        assert new_burger.ingredients[0]["ingredient_type"] == "SAUCE"

    @patch("praktikum.bun.Bun")
    @patch("praktikum.ingredient.Ingredient")
    def test_get_price(self, mock_bun, mock_ingredient, new_burger):
        new_burger.bun =  mock_bun
        new_burger.ingredients = [mock_ingredient]
        mock_bun.get_price.return_value = DataBun.BUN_PRICE
        mock_ingredient.get_price.return_value = DataIngredient.INGREDIENT_PRICE
        assert new_burger.get_price() == DataIngredient.INGREDIENT_PRICE + DataBun.BUN_PRICE * 2

    @patch("praktikum.bun.Bun")
    @patch("praktikum.ingredient.Ingredient")
    @patch("praktikum.burger.Burger.get_price", return_value=DataBurger.BURGER_PRICE)
    def test_get_receipt(self, mock_bun, mock_ingredient, mock_get_price,new_burger):
        new_burger.bun = mock_bun
        new_burger.ingredients = [mock_ingredient]
        mock_bun.get_name.return_value = DataBun.BUN_NAME
        mock_ingredient.get_type.return_value = DataIngredient.INGREDIENT_TYPE_SAUCE.lower()
        mock_ingredient.get_name.return_value = DataIngredient.INGREDIENT_NAME
        assert new_burger.get_receipt() == DataBurger.BURGER_RECEIPT
