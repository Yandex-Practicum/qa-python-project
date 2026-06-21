from unittest.mock import patch

from database import Database
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


def test_database_initialization_calls_bun_and_ingredient_constructors():
    with patch("database.Bun") as bun_mock, patch("database.Ingredient") as ingredient_mock:
        database = Database()

    assert bun_mock.call_count == 3
    assert ingredient_mock.call_count == 6
    assert len(database.buns) == 3
    assert len(database.ingredients) == 6


def test_database_initialization_uses_expected_ingredient_types_order():
    with patch("database.Bun"), patch("database.Ingredient") as ingredient_mock:
        Database()

    actual_types = [call.args[0] for call in ingredient_mock.call_args_list]

    assert actual_types == [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
        INGREDIENT_TYPE_FILLING,
        INGREDIENT_TYPE_FILLING,
    ]


def test_available_buns_returns_same_list_instance():
    database = Database()

    buns = database.available_buns()

    assert buns is database.buns


def test_available_ingredients_returns_same_list_instance():
    database = Database()

    ingredients = database.available_ingredients()

    assert ingredients is database.ingredients
