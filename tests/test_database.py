import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database


class TestDatabase:

    def test_initialize_buns(self):
        db = Database()
        assert len(db.buns) == 3
        assert db.buns[0].name == "black bun"
        assert db.buns[1].name == "white bun"
        assert db.buns[2].name == "red bun"

    def test_initialize_ingredients(self):
        db = Database()
        assert len(db.ingredients) == 6
        assert db.ingredients[0].name == "hot sauce"
        assert db.ingredients[1].name == "sour cream"
        assert db.ingredients[2].name == "chili sauce"
        assert db.ingredients[3].name == "cutlet"
        assert db.ingredients[4].name == "dinosaur"
        assert db.ingredients[5].name == "sausage"

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].name == "black bun"
        assert buns[1].name == "white bun"
        assert buns[2].name == "red bun"

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].name == "hot sauce"
        assert ingredients[1].name == "sour cream"
        assert ingredients[2].name == "chili sauce"
        assert ingredients[3].name == "cutlet"
        assert ingredients[4].name == "dinosaur"
        assert ingredients[5].name == "sausage"

    def test_add_bun(self):
        db = Database()
        new_bun = Bun("sesame bun", 150)
        db.buns.append(new_bun)
        assert len(db.buns) == 4
        assert db.buns[3].name == "sesame bun"

    def test_add_sauce_ingredient(self):
        db = Database()
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "mustard", 50)
        db.ingredients.append(new_ingredient)
        assert len(db.ingredients) == 7
        assert db.ingredients[6].name == "mustard"
        assert db.ingredients[6].type == INGREDIENT_TYPE_SAUCE

    def test_add_filling_ingredient(self):
        db = Database()
        new_filling_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "chicken", 120)
        db.ingredients.append(new_filling_ingredient)
        assert len(db.ingredients) == 7
        assert db.ingredients[6].name == "chicken"
        assert db.ingredients[6].type == INGREDIENT_TYPE_FILLING