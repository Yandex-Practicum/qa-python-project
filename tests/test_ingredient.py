import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient

def test_ingredient_creation():
    ingredient = Ingredient(ingredient_type="FILLING", name="Cheese", price=1.5)
    assert ingredient.get_type() == "FILLING"
    assert ingredient.get_name() == "Cheese"
    assert ingredient.get_price() == 1.5

def test_ingredient_get_name():
    ingredient = Ingredient(ingredient_type="SAUCE", name="Ketchup", price=0.5)
    assert ingredient.get_name() == "Ketchup"

def test_ingredient_get_type():
    ingredient = Ingredient(ingredient_type="SAUCE", name="Mayonnaise", price=0.7)
    assert ingredient.get_type() == "SAUCE"

def test_ingredient_get_price():
    ingredient = Ingredient(ingredient_type="FILLING", name="Bacon", price=2.0)
    assert ingredient.get_price() == 2.0

@pytest.mark.parametrize("ingredient_type, name, price, expected_price", [
    ("FILLING", "Cheese", 1.0, 1.0),
    ("SAUCE", "Ketchup", 0.5, 0.5),
    ("FILLING", "Bacon", 2.0, 2.0)
])
def test_ingredient_get_price_param(ingredient_type, name, price, expected_price):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    assert ingredient.get_price() == expected_price

def test_ingredient_mock_in_burger():
    ingredient_mock = Mock(spec=Ingredient)
    ingredient_mock.get_name.return_value = "Lettuce"
    ingredient_mock.get_type.return_value = "FILLING"
    ingredient_mock.get_price.return_value = 0.8

    assert ingredient_mock.get_name() == "Lettuce"
    assert ingredient_mock.get_type() == "FILLING"
    assert ingredient_mock.get_price() == 0.8
