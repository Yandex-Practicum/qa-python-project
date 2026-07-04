import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ],
)
def test_ingredient_initialization_sets_attributes(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 50),
        (INGREDIENT_TYPE_FILLING, "onion", 30),
    ],
)
def test_get_name_returns_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "ketchup", 50),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    ],
)
def test_get_type_returns_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize("price", [10, 99.9, 300])
def test_get_price_returns_price(price):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "ketchup", price)

    assert ingredient.get_price() == price
