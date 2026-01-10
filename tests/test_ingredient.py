import pytest
from praktikum.ingredient import Ingredient

class TestIngredients:
    def test_ingredient_initialization(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_get_name(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    def test_get_type(self, ingredient_data):
        ingredient_type, name, price = ingredient_data
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type