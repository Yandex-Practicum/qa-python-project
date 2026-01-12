import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "name, ingredient_type, price",
    [
        ("sauce", INGREDIENT_TYPE_SAUCE, 50),
        ("filling", INGREDIENT_TYPE_FILLING, 100),
    ]
)
def test_ingredient_fields(name, ingredient_type, price):
    ingredient = Ingredient(
        name=name,
        ingredient_type=ingredient_type,
        price=price
    )

    assert ingredient.name == name
    assert ingredient.type == ingredient_type
    assert ingredient.price == price
