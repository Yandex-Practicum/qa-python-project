from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_three_buns(self):
        database = Database()

        buns = database.available_buns()

        assert len(buns) == 3

    def test_available_ingredients_returns_six_ingredients(self):
        database = Database()

        ingredients = database.available_ingredients()

        assert len(ingredients) == 6