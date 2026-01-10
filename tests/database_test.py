class TestDatabase:

    def test_available_buns_quantity_3(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_quantity_6(self, database):
        assert len(database.available_ingredients()) == 6
