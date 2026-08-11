import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize(
    'ingredient_type, name, price',
    [
        (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
        (INGREDIENT_TYPE_FILLING, 'cutlet', 250.5),
    ],
)
def test_ingredient_returns_type_name_and_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
