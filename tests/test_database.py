class TestDatabase:

    def test_available_buns_returns_list_of_buns(self, mocked_db):
        result = mocked_db.available_buns()
        assert result == mocked_db.available_buns.return_value

    def test_available_ingredients_returns_list_of_ingredients(self, mocked_db):
        result = mocked_db.available_ingredients()
        assert result == mocked_db.available_ingredients.return_value