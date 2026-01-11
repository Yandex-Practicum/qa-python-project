import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @pytest.mark.parametrize(
        'price',
        [
            '100',
            '200',
            '300',
            '100.5',
            '200.78'
        ]
    )
    def test_get_price_true(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'hot sauce', price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        'name',
        [
            'hot sauce',
            'sour cream',
            'chili sauce',
            'cutlet',
            'dinosaur',
            'sausage'
        ]
    )
    def test_get_price_true(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 200)

        assert ingredient.get_name() == name


    @pytest.mark.parametrize(
        'type',
        [
            'INGREDIENT_TYPE_SAUCE',
            'INGREDIENT_TYPE_FILLING'
        ]
    )
    def test_get_type_true(self, type):
        ingredient = Ingredient(type, 'hot sauce', 100)

        assert ingredient.get_type() == type

