
import pytest

import ingredient_types
from ingredient import Ingredient
from helpers import *

class TestIngredient:
    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_price_correct_price_exist(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_name_correct_name_exist(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        'ingredient_type',
        [
            ingredient_types.INGREDIENT_TYPE_SAUCE,
            ingredient_types.INGREDIENT_TYPE_FILLING
        ]
    )
    def test_get_type_correct_type_exist(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)

        assert ingredient.get_type() == ingredient_type
