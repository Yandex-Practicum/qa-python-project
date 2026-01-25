import pytest

from data.ingredients import ingredients
from praktikum.ingredient import Ingredient


class TestIngredient:
    @pytest.mark.parametrize('ingredient_type, name, price', ingredients)
    def test_ingredient_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize('ingredient_type, name, price', ingredients)
    def test_ingredient_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize('ingredient_type, name, price', ingredients)
    def test_ingredient_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
