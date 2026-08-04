import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_TEST_DATA


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.type == ingredient_type
    assert ingredient.name == name
    assert ingredient.price == price


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
