from praktikum.database import Database


class TestDatabase:

    def test_available_buns_return_list_buns(self):
        database = Database()
        actual_result = len(database.available_buns())
        assert actual_result == 3

    def test_available_ingredients_return_list_ingredients(self):
        ingredients = Database()
        actual_result = len(ingredients.available_ingredients())
        assert actual_result == 6