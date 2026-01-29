import pytest

from data import Data
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestClassIngredient:
    # Тестируем получение типа ингредиента
    @pytest.mark.parametrize('type, name, price, expected_type',
                             [
                                 [INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_SPICE, Data.SPICE_PRICE, 'SAUCE'],
                                 [INGREDIENT_TYPE_FILLING, Data.INGREDIENT_METEORIT, Data.METEORIT_PRICE, 'FILLING']
                             ])
    def test_get_type_ingredient_create_object_parametrize_get_correct_type(self, type, name, price, expected_type):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_type

    # Тестируем получение имени ингредиента
    def test_get_name_create_object_ingredient_get_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, Data.INGREDIENT_SPICE, Data.SPICE_PRICE)
        assert ingredient.get_name() == 'Соус Spicy-X'

    # Тестируем получение цены ингредиента
    def test_get_price_create_object_ingredient_get_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, Data.INGREDIENT_METEORIT, Data.METEORIT_PRICE)
        assert ingredient.get_price() == 300

