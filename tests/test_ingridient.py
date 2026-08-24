import pytest
from praktikum.ingredient import Ingredient
from data import TestData

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', TestData.ingredients)
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
