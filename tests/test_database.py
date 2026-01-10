import pytest
from praktikum.database import Database


class TestDatabase:
    def test_available_buns_length(self):
        database = Database()
        assert len(database.available_buns()) == 3, "Неверное количество булочек"

    def test_available_ingredients_length(self):
        database = Database()
        assert len(database.available_ingredients()) == 6, "Неверное количество ингредиентов"
