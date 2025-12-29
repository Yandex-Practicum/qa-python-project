import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


INGREDIENT_DATA = [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 200),
]


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
def test_ingredient_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
def test_ingredient_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_DATA)
def test_ingredient_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price