import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENT_TEST_DATA


@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENT_TEST_DATA)
def test_ingredient_initialization(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
