from praktikum.database import Database

class TestDatabase:

    def test_available_buns_list(self):
        database = Database()
        available_buns = database.available_buns()
        assert len(available_buns) == 3

    def test_available_ingredients_list(self):
        database = Database()
        available_ingredients = database.available_ingredients()
        assert len(available_ingredients) == 6
