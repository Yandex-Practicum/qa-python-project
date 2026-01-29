import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:
    def test_get_price_correct_price(self):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Дипломный', 100)
        assert new_ingredient.get_price() == 100

    def test_get_name_correct_name(self):
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус Дипломный', 100)
        assert new_ingredient.get_name() == 'Соус Дипломный'

    @pytest.mark.parametrize('type, type_name', ([INGREDIENT_TYPE_SAUCE, 'SAUCE'], [INGREDIENT_TYPE_FILLING, 'FILLING']))
    def test_get_type_correct_type(self, type, type_name):
        ingredient = Ingredient(type, 'Начинка Дипломная', 200)
        assert ingredient.get_type() == type_name
