import pytest
from praktikum.ingredient import Ingredient
from tests.test_data import INGREDIENTS_DATA

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_DATA)
    def test_ingredient_points_valid(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

