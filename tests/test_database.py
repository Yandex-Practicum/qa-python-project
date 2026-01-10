from praktikum.database import Database


class TestDatabase:

    def test_check_available_buns_successful(self):
        database = Database()
        assert len(database.available_buns()) == 3

    def test_check_available_ingredients_successful(self):
        database = Database()
        assert len(database.available_ingredients()) == 6