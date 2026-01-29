from praktikum.database import Database


class TestDatabase:

    def test_available_buns_count(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_available_ingredients_count(self):
        database = Database()
        assert len(database.available_ingredients()) == 6
