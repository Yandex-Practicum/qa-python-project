from conftest import database


class TestDatabase:
    def test_available_buns(self, database):
        buns = database.available_buns()
        assert buns

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert ingredients
