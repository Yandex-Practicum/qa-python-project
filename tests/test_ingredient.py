import pytest
from Diplom_1.praktikum.ingredient import Ingredient


@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "hot sauce", 100),
    ("SAUCE", "sour cream", 200),
    ("FILLING", "cutlet", 100),
])
def test_ingredient_init(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price


@pytest.mark.parametrize("name", [
    ("hot sauce"),
    ("sour cream"),
    ("cutlet"),
])
def test_ingredient_get_name(name):
    ingredient = Ingredient("SAUCE", name, 100)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("price", [
    (100),
    (200),
    (300),
])
def test_ingredient_get_price(price):
    ingredient = Ingredient("SAUCE", "ingredient", price)
    assert ingredient.get_price() == price


@pytest.mark.parametrize("ingredient_type", [
    ("SAUCE"),
    ("FILLING"),
])
def test_ingredient_get_type(ingredient_type):
    ingredient = Ingredient(ingredient_type, "ingredient", 100)
    assert ingredient.get_type() == ingredient_type
