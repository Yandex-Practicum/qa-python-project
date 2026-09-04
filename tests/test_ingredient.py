import pytest

from praktikum.ingredient import Ingredient
from tests.data import INGREDIENT_CASES


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_type_returns_given_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_name_returns_given_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_CASES)
    def test_get_price_returns_given_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price
