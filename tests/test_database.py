import pytest

from Diplom_1.praktikum.database import Database

class TestDatabase:
    def test_available_buns(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()
        assert len(database.available_ingredients()) == 6