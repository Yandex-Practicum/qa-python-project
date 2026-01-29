class TestDatabase:
    def test_available_buns(self, database):
        db = database.available_buns()
        assert len(db) == 3


    def test_available_ingredients(self, database):
        db = database.available_ingredients()
        assert len(db) == 6


