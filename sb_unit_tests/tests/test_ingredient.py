import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 10.0),
        (INGREDIENT_TYPE_SAUCE, "mayo", 0.0),
        (INGREDIENT_TYPE_FILLING, "beef", 199.5),
        (INGREDIENT_TYPE_FILLING, "cheese", 1.25),
    ],
)
class TestIngredient:
    def test_get_type(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_type() == ingredient_type

    def test_get_name(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_name() == name

    def test_get_price(self, ingredient_type, name, price):
        ing = Ingredient(ingredient_type, name, price)
        assert ing.get_price() == price

