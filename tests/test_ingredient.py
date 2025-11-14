import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    """ Тест на получение цен на ингридиент """
    def test_get_price_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_price() == 15

    """ Тест на получение наименования ингридиента """
    def test_get_name_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15)
        assert ingredient.get_name() == 'Соус традиционный галактический'

    """ Тест на получение типа ингридиента """
    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус традиционный галактический', 15, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Хрустящие минеральные кольца', 300, 'FILLING']
        ]
    )
    def test_get_type_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
        