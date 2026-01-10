import pytest
from ingredient import Ingredient

def test_ingredient_creation():
    ingredient = Ingredient("SAUCE", "hot sauce", 100)
    assert ingredient.get_type() == "SAUCE"
    assert ingredient.get_name() == "hot sauce"
    assert ingredient.get_price() == 100

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "hot sauce", 100),
    ("FILLING", "cutlet", 200),
])
def test_ingredient_parametrized(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
