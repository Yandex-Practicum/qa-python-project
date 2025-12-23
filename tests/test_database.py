from database import Database
from Prakticum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

class TestDatabase:
    @pytest.fixture
    def database(self):
        return Database()

    def test_available_buns_names(self, database):
        expected_names = ["black bun", "white bun", "red bun"]
        actual_names = [bun.name for bun in database.available_buns()]

        assert set(actual_names) == set(expected_names)

    def test_available_buns_prices(self, database):
        expected_prices = [100, 200, 300]
        actual_prices = [bun.price for bun in database.available_buns()]

        assert set(actual_prices) == set(expected_prices)

    def test_available_ingredients_types(self, database):
        expected_types = [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING]
        actual_types = [ingredient.type for ingredient in database.available_ingredients()]

        assert set(actual_types) == set(expected_types)

    def test_available_ingredients_names(self, database):
        expected_names = ["hot sauce", "sour cream", "chili sauce", "cutlet", "dinosaur", "sausage"]
        actual_names = [ingredient.name for ingredient in database.available_ingredients()]

        assert set(actual_names) == set(expected_names)

    def test_available_ingredients_prices(self, database):
        expected_prices = [100, 200, 300, 100, 200, 300]
        actual_prices = [ingredient.price for ingredient in database.available_ingredients()]

        assert set(actual_prices) == set(expected_prices)