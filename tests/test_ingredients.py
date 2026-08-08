import pytest
from praktikum.ingredient import Ingredient
from data import IngredientTestData


class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_data", [
        IngredientTestData.get_valid_sauce(),
        IngredientTestData.get_valid_filling(),
        IngredientTestData.get_invalid_ingredient(),
    ])
    def test_ingredient_creation(self, ingredient_data):
        ingredient = Ingredient(
            ingredient_data["ingredient_type"], 
            ingredient_data["name"], 
            ingredient_data["price"]
        )
        assert ingredient.get_type() == ingredient_data["ingredient_type"]
        assert ingredient.get_name() == ingredient_data["name"]
        assert ingredient.get_price() == ingredient_data["price"]

    def test_ingredient_get_type(self):
        ingredient_data = IngredientTestData.get_valid_sauce()
        ingredient = Ingredient(
            ingredient_data['ingredient_type'], 
            ingredient_data['name'], 
            ingredient_data['price']
        )
        assert ingredient.get_type() == ingredient_data['ingredient_type']

    def test_ingredient_get_name(self):
        ingredient_data = IngredientTestData.get_valid_sauce()
        ingredient = Ingredient(
            ingredient_data['ingredient_type'], 
            ingredient_data['name'], 
            ingredient_data['price']
        )
        assert ingredient.get_name() == ingredient_data['name']

    def test_ingredient_get_price(self):
        ingredient_data = IngredientTestData.get_valid_filling()
        ingredient = Ingredient(
            ingredient_data['ingredient_type'], 
            ingredient_data['name'], 
            ingredient_data['price']
        )
        assert ingredient.get_price() == ingredient_data['price']