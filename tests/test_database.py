from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        available_buns = Database().available_buns()
        assert len(available_buns) == 3
    def test_available_ingredients(self):
        available_ingredients = Database().available_ingredients()
        assert len(available_ingredients) == 6

