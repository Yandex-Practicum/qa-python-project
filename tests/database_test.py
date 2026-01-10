class TestDatabase:
    def test_available_buns_true(self, database):
        assert database.available_buns() != []

    def test_available_ingredients_true(self, database):
        assert database.available_ingredients() != []
