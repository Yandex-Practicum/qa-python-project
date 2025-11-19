import pytest
from praktikum.ingredient import Ingredient
from data import ingredients_type_name_price

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_price_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_price() == ingredient_price


    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_name_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_name() == ingredient_name


    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", ingredients_type_name_price)
    def test_get_type_add_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type=ingredient_type, name=ingredient_name, price=ingredient_price)
        assert ingredient.get_type() == ingredient_type