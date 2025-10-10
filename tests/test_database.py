from praktikum.database import Database

class TestDatabase:

    def test_available_buns_success(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_ingredients_success(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
