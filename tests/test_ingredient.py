from praktikum.ingredient import Ingredient
import pytest

@pytest.mark.parametrize("ingredient_type, name, price", [
    ("SAUCE", "hot sauce", 100),
    ("FILLING", "cutlet", 200),
    ("FILLING", "dinosaur", 300)
])
def test_ingredient_init(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

@pytest.mark.parametrize("ingredient_type, name, price, expected_price", [
    ("FILLING", "cutlet", 200, 200),
    ("SAUCE", "hot sauce", 100, 100)
])
def test_ingredient_get_price(ingredient_type, name, price, expected_price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_price() == expected_price

@pytest.mark.parametrize("ingredient_type, name, price, expected_name", [
    ("FILLING", "dinosaur", 300, "dinosaur"),
    ("SAUCE", "hot sauce", 100, "hot sauce")
])
def test_ingredient_get_name(ingredient_type, name, price, expected_name):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == expected_name

def test_ingredient_init_with_empty_strings_and_zero_price():
    ingredient = Ingredient("", "", 0)
    assert ingredient.get_type() == ""
    assert ingredient.get_name() == ""
    assert ingredient.get_price() == 0





