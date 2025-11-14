import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    @pytest.mark.parametrize('type, result', ([INGREDIENT_TYPE_SAUCE, 'SAUCE'], [INGREDIENT_TYPE_FILLING, 'FILLING']))
    def test_get_type_correct_type(self, type, result):
        ingredient = Ingredient(type, 'ингредиент', 10)
        assert ingredient.get_type() == result

    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Чепотле', 15)
        assert ingredient.get_name() == 'Чепотле'

    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Сыр', 20)
        assert ingredient.get_price() == 20