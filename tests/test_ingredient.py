import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize("type_, name, price", [
    pytest.param(INGREDIENT_TYPE_SAUCE, "hot sauce", 100, id="sauce"),
    pytest.param(INGREDIENT_TYPE_FILLING, "cutlet", 250.5, id="filling"),
])
def test_ingredient_getters(type_, name, price):
    ingredient = Ingredient(type_, name, price)

    assert ingredient.get_type() == type_
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    