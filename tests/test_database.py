import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


EXPECTED_BUNS = [
    (0, "black bun", 100),
    (1, "white bun", 200),
    (2, "red bun", 300),
]

EXPECTED_INGREDIENTS = [
    (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
]


class TestDatabase:

    def test_available_buns_returns_three_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == 3

    @pytest.mark.parametrize("index, expected_name, expected_price", EXPECTED_BUNS)
    def test_available_buns_returns_buns_with_correct_name(self, index, expected_name, expected_price):
        database = Database()
        bun = database.available_buns()[index]

        assert bun.get_name() == expected_name

    @pytest.mark.parametrize("index, expected_name, expected_price", EXPECTED_BUNS)
    def test_available_buns_returns_buns_with_correct_price(self, index, expected_name, expected_price):
        database = Database()
        bun = database.available_buns()[index]

        assert bun.get_price() == expected_price

    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == 6

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        EXPECTED_INGREDIENTS
    )
    def test_available_ingredients_returns_ingredients_with_correct_type(
        self,
        index,
        expected_type,
        expected_name,
        expected_price
    ):
        database = Database()
        ingredient = database.available_ingredients()[index]

        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        EXPECTED_INGREDIENTS
    )
    def test_available_ingredients_returns_ingredients_with_correct_name(
        self,
        index,
        expected_type,
        expected_name,
        expected_price
    ):
        database = Database()
        ingredient = database.available_ingredients()[index]

        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        EXPECTED_INGREDIENTS
    )
    def test_available_ingredients_returns_ingredients_with_correct_price(
        self,
        index,
        expected_type,
        expected_name,
        expected_price
    ):
        database = Database()
        ingredient = database.available_ingredients()[index]

        assert ingredient.get_price() == expected_price