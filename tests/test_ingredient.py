import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize(
    "type_, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "мифический биоконцентрат", 4200),
    ],
)
def test_ingredient_get_name(type_, name, price):
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize(
    "type_, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "мифический биоконцентрат", 4200),
    ],
)
def test_ingredient_get_price(type_, name, price):
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_price() == price


@pytest.mark.parametrize(
    "type_, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "мифический биоконцентрат", 4200),
    ],
)
def test_ingredient_get_type(type_, name, price):
    ingredient = Ingredient(type_, name, price)
    assert ingredient.get_type() == type_
