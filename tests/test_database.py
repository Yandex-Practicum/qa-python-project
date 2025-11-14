import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

def test_database_initialization():
    db = Database()

    assert len(db.buns) == 3
    assert len(db.ingredients) == 6

    assert db.buns[0].get_name() == "black bun"
    assert db.buns[1].get_name() == "white bun"
    assert db.buns[2].get_name() == "red bun"

    assert db.ingredients[0].get_name() == "hot sauce"
    assert db.ingredients[3].get_name() == "cutlet"

def test_available_buns():
    db = Database()

    buns = db.available_buns()

    assert len(buns) == 3
    assert buns[0].get_name() == "black bun"
    assert buns[1].get_name() == "white bun"
    assert buns[2].get_name() == "red bun"

def test_available_ingredients():
    db = Database()

    ingredients = db.available_ingredients()

    assert len(ingredients) == 6
    assert ingredients[0].get_name() == "hot sauce"
    assert ingredients[3].get_name() == "cutlet"

def test_ingredient_types():
    db = Database()

    sauce_ingredients = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
    filling_ingredients = [ing for ing in db.ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]

    assert len(sauce_ingredients) == 3
    assert sauce_ingredients[0].get_name() == "hot sauce"
    assert sauce_ingredients[1].get_name() == "sour cream"

    assert len(filling_ingredients) == 3
    assert filling_ingredients[0].get_name() == "cutlet"
    assert filling_ingredients[2].get_name() == "sausage"


def test_available_buns_after_adding():
    db = Database()

    new_bun = Bun("sesame bun", 150)
    db.buns.append(new_bun)

    buns = db.available_buns()

    assert len(buns) == 4
    assert buns[3].get_name() == "sesame bun"
    assert buns[3].get_price() == 150

def test_available_ingredients_after_adding():
    db = Database()

    new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 50)
    db.ingredients.append(new_ingredient)

    ingredients = db.available_ingredients()

    assert len(ingredients) == 7
    assert ingredients[6].get_name() == "mustard"
    assert ingredients[6].get_price() == 50
