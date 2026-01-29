from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from helpers import get_ingredient_count_by_type, get_bun_names

class TestDatabase:

    def test_add_buns(self):
        db = Database()

        expected_count = 3
        actual_count = len(db.buns)
        assert actual_count == expected_count

        names = get_bun_names(db.buns)
        expected_names = ["black bun", "white bun", "red bun"]
        assert names == expected_names

    def test_add_ingredients(self):
        db = Database()

        expected_count = 6
        actual_count = len(db.ingredients)
        assert actual_count == expected_count

        sauce_count = get_ingredient_count_by_type(db.ingredients, INGREDIENT_TYPE_SAUCE)
        filling_count = get_ingredient_count_by_type(db.ingredients, INGREDIENT_TYPE_FILLING)

        assert sauce_count == 3
        assert filling_count == 3

    def test_get_all_ingredients(self):
        db = Database()

        count = len(db.ingredients)
        assert count == 6

    def test_available_ingredients(self):
        db = Database()

        ingredients = db.available_ingredients()

        expected_count = 6
        actual_count = len(ingredients)
        assert actual_count == expected_count

        sauce_count = get_ingredient_count_by_type(ingredients, INGREDIENT_TYPE_SAUCE)
        filling_count = get_ingredient_count_by_type(ingredients, INGREDIENT_TYPE_FILLING)

        assert sauce_count == 3
        assert filling_count == 3
