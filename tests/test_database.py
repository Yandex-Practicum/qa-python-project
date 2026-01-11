class TestDatabase:
    def test_init_database(self, database):
        assert database.buns[0].get_name() == "black bun"

    def test_available_buns_return_real_number_of_buns(self, database):
        assert len(database.available_buns()) == 3

    def test_available_ingredients_return_real_number_of_buns(self, database):
        assert len(database.available_ingredients()) == 6

