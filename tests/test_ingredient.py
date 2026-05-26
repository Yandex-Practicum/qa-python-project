import pytest 
from praktikum.ingredient import Ingredient
from data import IngredientData
#python -B -m pytest tests/test_ingredient.py

class TestIngredient:
    @pytest.mark.parametrize(
    "ingredient_sample",
    [
        IngredientData.hot_sauce,
        IngredientData.sour_cream
    ])
    def test_get_price(self, ingredient_sample):
        ingredient = Ingredient(*ingredient_sample)
        assert ingredient.get_price() == ingredient_sample[2]

    @pytest.mark.parametrize(
    "ingredient_sample",
    [
        IngredientData.chili_sauce,
        IngredientData.cutlet
    ])
    def test_get_name(self, ingredient_sample):
        ingredient = Ingredient(*ingredient_sample)
        assert ingredient.get_name() == ingredient_sample[1]

    @pytest.mark.parametrize(
    "ingredient_sample",
    [
        IngredientData.dinousaur,
        IngredientData.sausage
    ])
    def test_get_type(self, ingredient_sample):
        ingredient = Ingredient(*ingredient_sample)
        assert ingredient.get_type() == ingredient_sample[0]


