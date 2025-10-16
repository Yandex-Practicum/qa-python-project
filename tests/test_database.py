import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    def test_database_initialization_has_three_buns(self):
        database = Database()
        assert len(database.buns) == 3

    def test_database_initialization_has_six_ingredients(self):
        database = Database()
        assert len(database.ingredients) == 6

    def test_database_buns_are_bun_instances(self):
        database = Database()
        assert all(isinstance(bun, Bun) for bun in database.buns)

    def test_database_ingredients_are_ingredient_instances(self):
        database = Database()
        assert all(isinstance(ing, Ingredient) for ing in database.ingredients)

    def test_available_buns_returns_three_items(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_first_available_bun_is_black_bun(self):
        database = Database()
        assert database.available_buns()[0].get_name() == "black bun"

    def test_first_available_bun_has_correct_price(self):
        database = Database()
        assert database.available_buns()[0].get_price() == 100

    def test_available_ingredients_returns_six_items(self):
        database = Database()
        assert len(database.available_ingredients()) == 6

    def test_first_available_ingredient_is_hot_sauce(self):
        database = Database()
        assert database.available_ingredients()[0].get_name() == "hot sauce"

    def test_first_available_ingredient_has_correct_price(self):
        database = Database()
        assert database.available_ingredients()[0].get_price() == 100

    def test_first_available_ingredient_is_sauce_type(self):
        database = Database()
        assert database.available_ingredients()[0].get_type() == INGREDIENT_TYPE_SAUCE

    def test_fourth_available_ingredient_is_filling_type(self):
        database = Database()
        assert database.available_ingredients()[3].get_type() == INGREDIENT_TYPE_FILLING