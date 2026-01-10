from praktikum.database import Database


class TestDatabase:
    def test_available_buns_not_empty(self):
        database = Database()
        assert len(database.available_buns()) != 0

    def test_available_ingredients_not_empty(self):
        database = Database()
        assert database.available_ingredients() is not None

