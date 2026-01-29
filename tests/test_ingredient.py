import pytest
from ingredient import Ingredient
from data import DataIngredient

class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', DataIngredient.INGREDIENT_DATA)
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', DataIngredient.INGREDIENT_DATA)
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', DataIngredient.INGREDIENT_DATA)
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
