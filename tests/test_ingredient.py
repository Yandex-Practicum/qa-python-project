import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize('type_expected', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, ''])
    def test_get_type(self, type_expected):
        ingredient = Ingredient(type_expected, 'hot sauce', 1000)
        type_extracted = ingredient.get_type()

        assert type_expected == type_extracted

    @pytest.mark.parametrize('name_expected', ['test_name', ''])
    def test_get_name(self, name_expected):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name_expected, 1000)
        name_extracted = ingredient.get_name()

        assert name_expected == name_extracted

    @pytest.mark.parametrize('price_expected', [1000.0001, 0])
    def test_get_price(self, price_expected):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'sauce', price_expected)
        price_extracted = ingredient.get_price()

        assert price_expected == price_extracted
