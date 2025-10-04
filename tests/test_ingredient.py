import pytest

from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "ing_type, name, price, expected_type",
    [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100, INGREDIENT_TYPE_FILLING),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200, INGREDIENT_TYPE_FILLING),
        (INGREDIENT_TYPE_FILLING, "sausage", 300, INGREDIENT_TYPE_FILLING),
        ("CUSTOM", "strange", 0.0, "CUSTOM"),
    ],
)
def test_ingredient_getters(ing_type, name, price, expected_type):
    ingredient = Ingredient(ing_type, name, price)

    assert ingredient.get_type() == expected_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

