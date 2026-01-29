import pytest

from data import DataIngredient
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("type_ingredient", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_type_ingredient_true(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, DataIngredient.NAME_INGREDIENT,
                                DataIngredient.PRICE_INGREDIENT)
        assert ingredient.get_type() == type_ingredient

    def test_name_ingredient_true(self):
        ingredient = Ingredient(DataIngredient.random_type_ingredient(),
                                DataIngredient.NAME_INGREDIENT,
                                DataIngredient.PRICE_INGREDIENT)
        assert ingredient.get_name() == DataIngredient.NAME_INGREDIENT

    def test_price_ingredient_true(self):
        ingredient = Ingredient(DataIngredient.random_type_ingredient(),
                                DataIngredient.NAME_INGREDIENT,
                                DataIngredient.PRICE_INGREDIENT)
        assert ingredient.get_price() == DataIngredient.PRICE_INGREDIENT