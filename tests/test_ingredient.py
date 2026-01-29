import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'ingredient_name', 100.0)

        assert ingredient.get_type() == ingredient_type

    def test_get_price(self):
        ingredient = Ingredient('ingredient_type', 'ingredient_name', 100.0)

        assert ingredient.get_price() == 100.0

    def test_get_name(self):
        ingredient = Ingredient('ingredient_type', 'ingredient_name', 100.0)

        assert ingredient.get_name() == 'ingredient_name'

