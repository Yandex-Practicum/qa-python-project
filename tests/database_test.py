class TestDatabase:

    # тест на получение булок из базы данных
    def test_available_buns_true(self, put_buns_and_ingredients_into_database):
        database = put_buns_and_ingredients_into_database
        assert database.available_buns() == database.buns

    # тест на получение соусов из базы данных
    def test_available_ingredients_true(self, put_buns_and_ingredients_into_database):
        database = put_buns_and_ingredients_into_database
        assert database.available_ingredients() == database.ingredients
