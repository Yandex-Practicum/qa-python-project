from praktikum.database import Database

class TestDatabase:

    def test_get_available_buns(self):

        database = Database()

        assert database.available_buns()[0].name == "black bun"

    def test_get_available_ingredients(self):

        database = Database()

        assert database.available_ingredients()[0].name == "hot sauce"