from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:


    def test_database_initialized_with_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert isinstance(buns[0], Bun)


    def test_database_initialized_with_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)


    def test_buns_content(self):
        db = Database()
        buns = db.available_buns()

        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ]

        for i, (name, price) in enumerate(expected_buns):
            assert buns[i].get_name() == name
            assert buns[i].get_price() == price


    def test_ingredients_content(self):
        db = Database()
        ingredients = db.available_ingredients()

        expected_ingredients = [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

        for i, (ing_type, name, price) in enumerate(expected_ingredients):
            assert ingredients[i].get_type() == ing_type
            assert ingredients[i].get_name() == name
            assert ingredients[i].get_price() == price


    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)


    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)


