from unittest.mock import call, patch

import pytest

from praktikum.database import Database
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


class TestDatabaseInit:
    def test_creates_three_buns_with_correct_args(self):
        with patch("praktikum.database.Bun") as mock_bun:
            Database()

            assert mock_bun.call_count == 3
            mock_bun.assert_has_calls(
                [
                    call("black bun", 100),
                    call("white bun", 200),
                    call("red bun", 300),
                ]
            )

    def test_creates_six_ingredients_with_correct_args(self):
        with patch("praktikum.database.Ingredient") as mock_ingredient:
            Database()

            assert mock_ingredient.call_count == 6
            mock_ingredient.assert_has_calls(
                [
                    call(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
                    call(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
                    call(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
                    call(INGREDIENT_TYPE_FILLING, "cutlet", 100),
                    call(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
                    call(INGREDIENT_TYPE_FILLING, "sausage", 300),
                ],
                any_order=False,
            )


class TestDatabaseContent:
    def test_buns_count(self):
        assert len(Database().available_buns()) == 3

    def test_ingredients_count(self):
        assert len(Database().available_ingredients()) == 6

    @pytest.mark.parametrize(
        "index, expected_name, expected_price",
        [(0, "black bun", 100), (1, "white bun", 200), (2, "red bun", 300)],
        ids=["black", "white", "red"],
    )
    def test_bun_content(self, index, expected_name, expected_price):
        bun = Database().available_buns()[index]

        assert bun.get_name() == expected_name
        assert bun.get_price() == expected_price

    @pytest.mark.parametrize(
        "index, expected_type, expected_name, expected_price",
        [
            (0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (1, INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (3, INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (4, INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (5, INGREDIENT_TYPE_FILLING, "sausage", 300),
        ],
        ids=[
            "hot_sauce",
            "sour_cream",
            "chili_sauce",
            "cutlet",
            "dinosaur",
            "sausage",
        ],
    )
    def test_ingredient_content(
        self, index, expected_type, expected_name, expected_price
    ):
        ingredient = Database().available_ingredients()[index]

        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price


class TestDatabaseGetters:
    def test_available_buns_returns_internal_list(self):
        db = Database()

        assert db.available_buns() is db.buns

    def test_available_ingredients_returns_internal_list(self):
        db = Database()

        assert db.available_ingredients() is db.ingredients

    def test_instances_are_independent(self):
        db1 = Database()
        db2 = Database()

        assert db1.buns is not db2.buns
        assert db1.ingredients is not db2.ingredients

        db1.buns.append("fake")
        assert len(db1.buns) == 4
        assert len(db2.buns) == 3