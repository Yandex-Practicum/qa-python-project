from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:

    def test_get_price_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'test_filling', 20 )
        assert ingredient.get_price() == 20

    def test_get_name_true(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'test_sauce', 10)
        assert ingredient.get_name() == 'test_sauce'

    @pytest.mark.parametrize('type, name, price, type_ingredient',
    [
        [INGREDIENT_TYPE_FILLING, 'test_filling', 20, 'FILLING'],
        [INGREDIENT_TYPE_SAUCE, 'test_sauce', 10, 'SAUCE']
    ]
                             )
    def test_get_type_true(self, type, name, price, type_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type_ingredient


