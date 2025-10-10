import data


class TestDatabase:

    def test_available_buns(self, database):
        database.buns = data.LIST_BUNS
        assert len(database.available_buns()) == 4

    def test_available_ingredients(self, database):
        database.buns = data.LIST_INGREDIENTS
        assert len(database.available_buns()) == 3