import pytest
import random
from data import TestData
from praktikum.ingredient import Ingredient

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type", TestData.ingredient_types)
    def test_get_ingredient_price(self, ingredient_type):

        ingredient = Ingredient(ingredient_type, random.choice(TestData.ingredient_names), 100)

        assert ingredient.get_price() == 100

    @pytest.mark.parametrize("ingredient_type", TestData.ingredient_types)
    def test_get_ingredient_name(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "sour_cream", random.choice(TestData.prices))

        assert ingredient.get_name() == "sour_cream"

    @pytest.mark.parametrize("ingredient_type", TestData.ingredient_types)
    def test_get_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, random.choice(TestData.ingredient_names), random.choice(TestData.prices))

        assert ingredient.get_type() == ingredient_type