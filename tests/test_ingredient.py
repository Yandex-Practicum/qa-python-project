import pytest

from praktikum.ingredient import Ingredient
from tests.data import FILLING, SAUCE


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", FILLING + SAUCE)
    def test_get_type_returns_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", FILLING + SAUCE)
    def test_get_name_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", FILLING + SAUCE)
    def test_get_price_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price