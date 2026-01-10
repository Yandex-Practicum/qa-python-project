from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        data = Database()
        buns = data.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self):
        data = Database()
        ingredients = data.available_ingredients()
        assert len(ingredients) == 6