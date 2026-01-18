from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        database = Database()

        assert database.available_buns()
        assert len(database.available_buns()) == 3

    def test_available_ingredients(self):
        database = Database()

        assert database.available_ingredients()
        assert len(database.available_ingredients()) == 6
