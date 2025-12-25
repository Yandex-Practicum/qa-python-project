import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_data import (
    BUNS_COUNT,
    INGREDIENTS_COUNT
)

class TestDatabase:

    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()

        assert len(buns) == BUNS_COUNT
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()

        assert len(ingredients) == INGREDIENTS_COUNT
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)


