import pytest
from praktikum.ingredient import Ingredient
from constants import Constants


class TestIngredient:

    @pytest.mark.parametrize("ingredient_price,ingredient_name,ingredient_type", Constants.INGREDIENT)
    def test_ingredient_price(self, ingredient_price, ingredient_name, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.price == ingredient_price

    @pytest.mark.parametrize("ingredient_price,ingredient_name,ingredient_type", Constants.INGREDIENT)
    def test_ingredient_name(self, ingredient_price, ingredient_name, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.name == ingredient_name

    @pytest.mark.parametrize("ingredient_price,ingredient_name,ingredient_type", Constants.INGREDIENT)
    def test_ingredient_type(self, ingredient_price, ingredient_name, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.type == ingredient_type





