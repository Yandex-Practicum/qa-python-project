import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    'ingredient_type',
    [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ],
)
def test_get_type_returns_init_value(ingredient_type):
    ingredient = Ingredient(ingredient_type, 'test ingredient', 100.0)

    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize(
    'name',
    [
        'hot sauce',
        'котлета',
        'ingredient-123',
        'ingr!@#$',
    ],
)
def test_get_name_returns_init_value(name):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100.0)

    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    'price',
    [
        0,
        1,
        300.5,
        1_000_000.0,
        -10.5,
    ],
)
def test_get_price_returns_init_value(price):
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'test ingredient', price)

    assert ingredient.get_price() == price
