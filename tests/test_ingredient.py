import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_TEST_CASES

class TestIngredient:
    @pytest.mark.parametrize("name, type, price", INGREDIENT_TEST_CASES)
    def test_get_name(self, name, type, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("name, type, price", INGREDIENT_TEST_CASES)
    def test_get_price(self, name, type, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("name, type, price", INGREDIENT_TEST_CASES)
    def test_get_type(self, name, type, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
