from unittest.mock import patch

import pytest

from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_three_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_returns_six_ingredients(self, database):
        assert len(database.available_ingredients()) == 6

    @pytest.mark.parametrize(
        "index, name, price",
        [
            (0, "black bun", 100),
            (1, "white bun", 200),
            (2, "red bun", 300),
        ],
    )
    def test_bun_names_and_prices(self, database, index, name, price):
        bun = database.available_buns()[index]

        assert bun.get_name() == name
        assert bun.get_price() == price

    @pytest.mark.parametrize(
        "index, name, price",
        [
            (0, "hot sauce", 100),
            (3, "cutlet", 100),
            (5, "sausage", 300),
        ],
    )
    def test_ingredient_names_and_prices(self, database, index, name, price):
        ingredient = database.available_ingredients()[index]

        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    @patch("praktikum.database.Bun")
    @patch("praktikum.database.Ingredient")
    def test_init_creates_buns_and_ingredients(self, ingredient_mock, bun_mock):
        Database()

        assert bun_mock.call_count == 3
        assert ingredient_mock.call_count == 6
