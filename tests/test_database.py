from praktikum.database import Database

class TestDatabase:
    def test_available_buns_returns_not_empty_list(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) > 0

    def test_available_ingredients_returns_not_empty_list(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) > 0