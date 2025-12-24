import pytest
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_buns_are_returned_as_list(self, fresh_db):
        buns = fresh_db.available_buns()
        assert isinstance(buns, list)

    def test_ingredients_are_returned_as_list(self, fresh_db):
        items = fresh_db.available_ingredients()
        assert isinstance(items, list)

    def test_buns_count_is_expected(self, fresh_db):
        assert len(fresh_db.available_buns()) == 3

    @pytest.mark.parametrize("i,expected", [
        (0, "black bun"),
        (1, "white bun"),
        (2, "red bun"),
    ])
    def test_bun_names_are_correct(self, fresh_db, i, expected):
        buns = fresh_db.available_buns()
        assert buns[i].get_name() == expected

    def test_ingredients_count_is_expected(self, fresh_db):
        assert len(fresh_db.available_ingredients()) == 6

    @pytest.mark.parametrize("i,expected_type", [
        (0, INGREDIENT_TYPE_SAUCE),
        (3, INGREDIENT_TYPE_FILLING),
    ])
    def test_ingredient_types_are_accurate(self, fresh_db, i, expected_type):
        items = fresh_db.available_ingredients()
        assert items[i].get_type() == expected_type
