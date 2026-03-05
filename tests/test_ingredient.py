import pytest

from ingredient import Ingredient
from helpers.data import INGREDIENTS_INFO


class TestIngredient:

    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_INFO)
    def test_get_price_returns_price_of_ingredient(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["ingredient_type"], ingredient_data["ingredient_name"], ingredient_data["ingredient_price"])

        assert ingredient.get_price() == ingredient_data["ingredient_price"]


    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_INFO)
    def test_get_name_returns_name_of_ingredient(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["ingredient_type"], ingredient_data["ingredient_name"], ingredient_data["ingredient_price"])

        assert ingredient.get_name() == ingredient_data["ingredient_name"]


    @pytest.mark.parametrize("ingredient_data", INGREDIENTS_INFO)
    def test_get_type_returns_type_of_ingredient(self, ingredient_data):
        ingredient = Ingredient(ingredient_data["ingredient_type"], ingredient_data["ingredient_name"], ingredient_data["ingredient_price"])

        assert ingredient.get_type() == ingredient_data["ingredient_type"]