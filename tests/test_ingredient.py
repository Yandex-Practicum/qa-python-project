import pytest

from data import *
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('td_price', IngredientTestData.price)
    def test_get_price(self, td_price):
        ingredient = Ingredient('SAUCE', 'Безразличный майонез', td_price)
        assert ingredient.get_price() == td_price

    @pytest.mark.parametrize('td_name', IngredientTestData.ingredients)
    def test_get_name(self, td_name):
        ingredient = Ingredient('SAUCE', td_name, 100500)
        assert ingredient.get_name() == td_name

    @pytest.mark.parametrize('td_type', IngredientTestData.type)
    def test_get_type(self, td_type):
        ingredient = Ingredient(td_type, 'Безразличный майонез', 100500)
        assert ingredient.get_type() == td_type