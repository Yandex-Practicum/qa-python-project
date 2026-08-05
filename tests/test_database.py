from praktikum.database import Database

class TestDatabase:
    def test_database_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"

    def test_database_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[0].get_name() == "hot sauce"