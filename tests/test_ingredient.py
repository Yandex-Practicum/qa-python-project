import pytest

from data import *
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

class TestIngredient:

    @pytest.mark.parametrize(
        'ingredient_type, name, price, result',
        [
            [INGREDIENT_TYPE_SAUCE, 'sauce', 160, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'filling', 170, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, ingredient_type, name, price, result):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == result

    def test_get_price_ingredient(self, sauce):
        assert sauce.get_price() == 80

    def test_get_name_ingredient(self, topping):
        assert topping.get_name() == 'potato'