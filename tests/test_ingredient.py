import pytest
from praktikum.ingredient import Ingredient
from data import ingredient_type_first, ingredient_name_first, ingredient_price_first


class TestIngredients:


    def test_get_ingredient_type(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)

        assert ingredient.get_type() == ingredient_type_first

    def test_get_ingredient_name(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)

        assert ingredient.get_name() == ingredient_name_first


    def test_get_ingredient_price(self):
        ingredient = Ingredient(ingredient_type_first, ingredient_name_first, ingredient_price_first)

        assert ingredient.get_price() == ingredient_price_first


