import pytest
from database import Database
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    @pytest.mark.parametrize(
        "bun_index, expected_name",
        [
            (0, "black bun"),
            (1, "white bun"),
            (2, "red bun")
        ]
    )
    def test_available_buns(self, bun_index, expected_name):
        database = Database()
        buns = database.available_buns()
        assert buns[bun_index].get_name() == expected_name

    @pytest.mark.parametrize(
        "ingredient_index, expected_name, expected_type",
        [
            (0, "hot sauce", INGREDIENT_TYPE_SAUCE),
            (3, "cutlet", INGREDIENT_TYPE_FILLING),
            (5, "sausage", INGREDIENT_TYPE_FILLING)
        ]
    )
    def test_available_ingredients(self, ingredient_index, expected_name, expected_type):
        database = Database()
        ingredients = database.available_ingredients()
        assert ingredients[ingredient_index].get_name() == expected_name
        assert ingredients[ingredient_index].get_type() == expected_type
