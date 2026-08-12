import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_DATA1, INGREDIENT_DATA2, INGREDIENT_DATA3

class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_DATA1["ingredient_type"], INGREDIENT_DATA1["name"], INGREDIENT_DATA1["price"]),
        (INGREDIENT_DATA2["ingredient_type"], INGREDIENT_DATA2["name"], INGREDIENT_DATA2["price"]),
        (INGREDIENT_DATA3["ingredient_type"], INGREDIENT_DATA3["name"], INGREDIENT_DATA3["price"])
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_get_type(self):
        ingredient = Ingredient(INGREDIENT_DATA1['ingredient_type'], INGREDIENT_DATA1['name'], INGREDIENT_DATA1['price'])
        assert ingredient.get_type() == INGREDIENT_DATA1['ingredient_type']

    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_DATA1['ingredient_type'], INGREDIENT_DATA1['name'], INGREDIENT_DATA1['price'])
        assert ingredient.get_name() == INGREDIENT_DATA1['name']

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_DATA2['ingredient_type'], INGREDIENT_DATA2['name'], INGREDIENT_DATA2['price'])
        assert ingredient.get_price() == INGREDIENT_DATA2['price']
