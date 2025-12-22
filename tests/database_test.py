import pytest
from unittest.mock import patch

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


def test_available_buns_returns_list_of_buns():
    database = Database()

    buns = database.available_buns()

    assert isinstance(buns, list)
    assert len(buns) == 3
    assert all(isinstance(bun, Bun) for bun in buns)


def test_available_ingredients_returns_list_of_ingredients():
    database = Database()

    ingredients = database.available_ingredients()

    assert isinstance(ingredients, list)
    assert len(ingredients) == 6
    assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)


@patch("praktikum.database.Bun")
@patch("praktikum.database.Ingredient")
def test_database_initializes_data(mock_ingredient, mock_bun):
    Database()

    assert mock_bun.call_count == 3
    assert mock_ingredient.call_count == 6
