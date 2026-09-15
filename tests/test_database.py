import pytest
from praktikum.database import Database

class TestDatabase:
    def test_available_buns_returns_correct_list_and_count(self):
        db = Database()

        buns_list = db.available_buns()
        assert type(buns_list) is list
        assert len(buns_list) == 3
        assert buns_list[0].get_name() == "black bun"

    def test_available_ingredients_returns_correct_list_and_count(self):
        db = Database()
        ingredients_list = db.available_ingredients()
        assert type(ingredients_list) is list
        assert len(ingredients_list) == 6

        assert ingredients_list[3].get_name() == "cutlet"
        assert ingredients_list[3].get_type() == "FILLING"
