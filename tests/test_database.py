import pytest
from praktikumm.database import Database
from praktikumm.bun import Bun
from praktikumm.ingredient import Ingredient

def test_available_buns():
    db = Database()
    buns = db.available_buns()
    assert len(buns) == 3
    assert isinstance(buns[0], Bun)

def test_available_ingredients():
    db = Database()
    ingredients = db.available_ingredients()
    assert len(ingredients) == 6
    assert isinstance(ingredients[0], Ingredient)

def test_buns_have_correct_data():
    db = Database()
    bun = db.available_buns()[0]
    assert bun.get_name() == "black bun"
    assert bun.get_price() == 100

def test_ingredients_have_correct_data():
    db = Database()
    ingredient = db.available_ingredients()[0]
    assert ingredient.get_type() == "SAUCE"
    assert ingredient.get_name() == "hot sauce"
    assert ingredient.get_price() == 100