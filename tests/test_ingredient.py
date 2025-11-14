import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


@pytest.mark.parametrize('ingredient_type, name, price', [
        [INGREDIENT_TYPE_SAUCE, "hot sauce", 88.25],
        [INGREDIENT_TYPE_FILLING, "dinosaur", -100.78]
    ])
class TestIngredient:

    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
