import pytest
from praktikum.ingredient import Ingredient
from data import IngredientsData

class TestIngredient:
    @pytest.mark.parametrize("type, name, price", IngredientsData.ingredients_data)
    def test_get_price_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("type, name, price", IngredientsData.ingredients_data)
    def test_get_name_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("type, name, price", IngredientsData.ingredients_data)
    def test_get_type_ingredient(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type