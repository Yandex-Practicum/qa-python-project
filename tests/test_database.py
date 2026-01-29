from praktikum.database import Database


class TestDatabases:

    def test_available_buns_true(self):
        database = Database()

        assert database.available_buns() == database.buns

    def test_available_ingredients_true(self):
        database = Database()

        assert database.available_ingredients() == database.ingredients