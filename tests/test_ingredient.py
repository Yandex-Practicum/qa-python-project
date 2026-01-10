import pytest

from data import IngredientData
from praktikum.ingredient import Ingredient

class TestIngredient:

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.ingredient_list[0],
                                                              IngredientData.ingredient_list[3]])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.ingredient_list[1],
                                                              IngredientData.ingredient_list[4]])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', [IngredientData.ingredient_list[2],
                                                              IngredientData.ingredient_list[5]])
    def test_ingredient_get_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type