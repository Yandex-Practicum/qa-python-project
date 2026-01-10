import pytest
from praktikum.ingredient import Ingredient
from data import Data


@pytest.mark.parametrize("ingredient_type, name, price", Data.INGREDIENTS)
def test_get_name(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name


@pytest.mark.parametrize("ingredient_type, name, price", Data.INGREDIENTS)
def test_get_type(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type


@pytest.mark.parametrize("ingredient_type, name, price", Data.INGREDIENTS)
def test_get_price(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == price