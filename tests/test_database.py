from helpers import filter_ingredients_by_type
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_get_available_buns(self):
        database_buns = Database()
        available_buns = database_buns.available_buns()
        assert len(available_buns) == 3

    def test_get_all_available_ingredients(self):
        database_ingredients = Database()
        available_ingredients = database_ingredients.available_ingredients()
        assert len(available_ingredients) == 6

    def test_get_available_sauces_from_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        sauces = filter_ingredients_by_type(available_ingredients, INGREDIENT_TYPE_SAUCE)
        assert len(sauces) == 3

    def test_get_available_fillings_from_ingredients(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        fillings = filter_ingredients_by_type(available_ingredients, INGREDIENT_TYPE_FILLING)
        assert len(fillings) == 3

