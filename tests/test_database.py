from praktikum.database import Database


class TestDatabase:
    def test_available_buns(self):
        data_base = Database()
        buns = data_base.available_buns()
        assert len(buns) > 0

    def test_available_ingredients(self):
        data_base = Database()
        ingredients = data_base.available_ingredients()
        assert len(ingredients) > 0
