class TestDatabase:

    def test_available_buns_correct_total(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_correct_total(self, database):
        assert len(database.available_ingredients()) == 6
