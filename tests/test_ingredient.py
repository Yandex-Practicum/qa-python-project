import pytest
from praktikumm.ingredient import Ingredient

def test_ingredient_get_name():
    ingredient = Ingredient("SAUCE", "hot sauce", 100)
    assert ingredient.get_name() == "hot sauce"

def test_ingredient_get_price():
    ingredient = Ingredient("FILLING", "sausage", 300)
    assert ingredient.get_price() == 300

def test_ingredient_get_type():
    ingredient = Ingredient("SAUCE", "sour cream", 150)
    assert ingredient.get_type() == "SAUCE"