import pytest
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database
from unittest.mock import Mock


class TestDatabase:

    def test_get_list_with_available_buns(self, create_new_database):
        assert len(create_new_database.available_buns()) == 3

    def test_get_list_with_available_ingredient(self, create_new_database):
        assert len(create_new_database.available_ingredients()) == 6