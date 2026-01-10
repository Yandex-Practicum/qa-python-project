from praktikum.database import Database


class TestDatabase:
    def test_available_buns_three_buns_buns_available(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_ingredients_six_ingredient_ingredients_available(self):
        database = Database()
        ingredient = database.available_ingredients()
        assert len(ingredient) == 6
