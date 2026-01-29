
from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        data = Database()
        assert data.available_buns() == data.buns

    def test_available_ingredients(self):
        data = Database()
        assert data.available_ingredients() == data.ingredients