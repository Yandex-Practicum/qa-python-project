from praktikum.database import Database
from praktikum.ingredient_types import (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)


class TestDatabase:

    def test_available_buns_returns_three_buns(self):
        database = Database()

        buns = database.available_buns()

        assert len(buns) == 3

    def test_available_buns_returns_correct_bun_names(self):
        database = Database()

        buns = database.available_buns()

        assert buns[0].get_name() == 'black bun'
        assert buns[1].get_name() == 'white bun'
        assert buns[2].get_name() == 'red bun'

    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    def test_available_ingredients_returns_correct_ingredient_types(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING