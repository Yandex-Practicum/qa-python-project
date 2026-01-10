from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import Data
import pytest


class TestIngredient:

    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.ingredient_name, Data.ingredient_price_2)
    @pytest.mark.parametrize("ingredient_method, result",
                             [(ingredient.get_price(), 10), (ingredient.get_name(), 'hot sauce'), (ingredient.get_type(), 'SAUCE')])
    def test_get_price(self, ingredient_method, result):
        ingredient_component = ingredient_method

        assert ingredient_component == result
