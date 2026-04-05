import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING
)


class TestIngredient:

    @pytest.mark.parametrize('name', [
        'hot sauce',
        'cutlet',
        'sour cream',
    ])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('price', [
        100,
        200,
        50.5,
    ])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'test', price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type', [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, 'test', 100)
        assert ingredient.get_type() == ingredient_type