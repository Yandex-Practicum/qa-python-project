class TestDataBase:
    def test_available_buns(self, database):
        buns = database.available_buns()
        assert len(buns) == 3

    def test_available_ingredients(self, database):
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6
