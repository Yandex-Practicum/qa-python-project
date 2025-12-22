import pytest
from praktikum.ingredient import Ingredient


def test_ingredient_constructor():
    ingredient = Ingredient("sauce", "ketchup", 50)

    assert ingredient.type == "sauce"
    assert ingredient.name == "ketchup"
    assert ingredient.price == 50


def test_get_price():
    ingredient = Ingredient("filling", "cutlet", 100)

    assert ingredient.get_price() == 100


def test_get_name():
    ingredient = Ingredient("filling", "cheese", 70)

    assert ingredient.get_name() == "cheese"


def test_get_type():
    ingredient = Ingredient("sauce", "mustard", 30)

    assert ingredient.get_type() == "sauce"
