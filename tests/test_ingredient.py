import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    @pytest.mark.parametrize('price_ingredient', [0, 10])
    def test_get_price_for_ingredient(self, price_ingredient):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test_name", price_ingredient)
        assert ingredient.get_price() == price_ingredient

    def test_get_name_for_ingredient(self):
        expected_name = "test_name"
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, expected_name, 10)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize('type_ingredient', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_for_ingredient(self, type_ingredient):
        ingredient = Ingredient(type_ingredient, "test_name", 10)
        assert ingredient.get_type() == type_ingredient
