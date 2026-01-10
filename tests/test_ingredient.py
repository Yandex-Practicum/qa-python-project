import pytest
from practikum.ingredient import Ingredient
from conftest import TEST_INGREDIENTS


@pytest.mark.parametrize("ingredient_type, name, price", TEST_INGREDIENTS)
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

