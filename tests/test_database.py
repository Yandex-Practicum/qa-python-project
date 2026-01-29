from src.database import Database


class TestDataBase:

    def test_get_available_buns(self):
        db = Database()
        expected_buns = db.available_buns()

        assert db.buns == expected_buns
        assert len(expected_buns) == 3

    def test_get_available_ingredients(self):
        db = Database()
        expected_ingredients = db.available_ingredients()

        assert db.ingredients == expected_ingredients
        assert len(expected_ingredients) == 6
