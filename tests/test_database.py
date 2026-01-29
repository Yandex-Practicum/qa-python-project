class TestDatabase:

    def test_available_buns(self, database, mock_buns_list):
        database.buns = []
        database.buns.append(mock_buns_list)

        assert database.available_buns() == database.buns

    def test_available_ingredients(self, database, mock_ingredients_list):
        database.ingredients = []
        database.ingredients.append(mock_ingredients_list)

        assert database.available_ingredients() == database.ingredients
