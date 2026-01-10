import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    def test_ingredient_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 100)
        assert ingredient.get_name() == 'sour cream'

    def test_ingredient_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sour cream', 100)
        assert ingredient.get_price() == 100

    @pytest.mark.parametrize('ingredient_type, name, price, expectation', [
        [INGREDIENT_TYPE_SAUCE, 'sour cream', 100, INGREDIENT_TYPE_SAUCE],
        [INGREDIENT_TYPE_FILLING, "dinosaur", 200, INGREDIENT_TYPE_FILLING]
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price, expectation):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expectation
