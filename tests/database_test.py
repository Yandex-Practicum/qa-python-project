from data import test_data

class TestDatabase:
    def test_available_buns(self, database):
        assert len(database.available_buns()) == test_data.AVAILABLE_BUNS_COUNT

    def test_available_ingredients(selfself, database):
        assert len(database.available_ingredients()) == test_data.AVAILABLE_INGREDIENTS_COUNT