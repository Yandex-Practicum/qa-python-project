class TestDatabase:
    def test_available_buns(self, database):
        database = database.available_buns()
        assert len(database) == 3

    def test_available_ingredients(self, database):
        database = database.available_ingredients()
        assert len(database) == 6
