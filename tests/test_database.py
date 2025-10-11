from praktikum.database import Database

class TestDatabase:
    def test_databaser_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3
        assert buns[2].get_name() == "red bun"
        assert buns[0].get_price() == 100

    def test_database_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_type() == "SAUCE"
        assert ingredients[0].get_price() == 100