import pytest

from database import Database
import ingredient_types as types


class TestDatabase:
    def test_database_has_buns(self):
        database = Database()
        assert len(database.buns) == 3

    def test_database_has_ingredients(self):
        database = Database()
        assert len(database.ingredients) == 6

    def test_buns_data_correct(self):
        database = Database()
        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]

        for i, (expected_name, expected_price) in enumerate(expected_buns):
            assert database.buns[i].get_name() == expected_name
            assert database.buns[i].get_price() == expected_price

    def test_ingredients_data_correct(self):
        database = Database()
        expected_ingredients = [
            (types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (types.INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (types.INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (types.INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (types.INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        for i, (expected_type, expected_name, expected_price) in enumerate(expected_ingredients):
            assert database.ingredients[i].get_type() == expected_type
            assert database.ingredients[i].get_name() == expected_name
            assert database.ingredients[i].get_price() == expected_price

    def test_available_buns_return_all_buns(self):
        database = Database()
        expected_buns = [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300)
        ]

        for i, (expected_name, expected_price) in enumerate(expected_buns):
            assert database.buns[i].get_name() == expected_name
            assert database.buns[i].get_price() == expected_price

    def test_available_ingredients_return_all_ingredients(self):
        database = Database()
        expected_ingredients = [
            (types.INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (types.INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (types.INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (types.INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (types.INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (types.INGREDIENT_TYPE_FILLING, "sausage", 300)
        ]

        for i, (expected_type, expected_name, expected_price) in enumerate(expected_ingredients):
            assert database.ingredients[i].get_type() == expected_type
            assert database.ingredients[i].get_name() == expected_name
            assert database.ingredients[i].get_price() == expected_price
