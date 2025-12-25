from data import SAUCE_NAME, FILLING_NAME


class TestDatabase:
    def test_available_buns(self, database_with_buns_ingredients):
        database = database_with_buns_ingredients
        buns = database.available_buns()

        assert len(buns) == 6

    def test_available_ingredients(self, database_with_buns_ingredients):
        database = database_with_buns_ingredients
        ingredients = database.available_ingredients()

        assert ingredients[6].get_name() == SAUCE_NAME and ingredients[7].get_name() == FILLING_NAME

