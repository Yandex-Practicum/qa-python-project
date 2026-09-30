from praktikum.database import Database


class TestDatabase:

    def test_available_buns_count(self):
        db = Database()
        buns = db.available_buns()
        assert len(buns) == 3

    def test_available_buns_first_name(self):
        db = Database()
        buns = db.available_buns()
        assert buns[0].get_name() == "black bun"

    def test_available_ingredients_count(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_available_ingredients_first_name(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert ingredients[0].get_name() == "hot sauce"