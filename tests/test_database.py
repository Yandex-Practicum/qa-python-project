from data import BunData, IngredientData
from praktikum.database import Database

class TestDatabase:

    def test_database_available_buns_quantity(self):
        database = Database()
        buns_list = database.available_buns()
        assert len(buns_list) == 3

    def test_database_available_buns_correct_info(self):
        database = Database()
        buns = database.available_buns()
        expected_list = BunData.buns_list
        actual_list = []

        for one_bun in buns:
            one_bun_data = [one_bun.name, one_bun.price]
            actual_list.append(one_bun_data)

        assert actual_list == expected_list


    def test_database_available_ingredients_quantity(self):
        database = Database()
        ingredients_list = database.available_ingredients()
        assert len(ingredients_list) == 6

    def test_database_available_ingredients_correct_info(self):
        database = Database()
        ingredients = database.available_ingredients()
        expected_list = IngredientData.ingredient_list
        actual_list = []

        for one_ingredient in ingredients:
            one_ingredient_data = [one_ingredient.type, one_ingredient.name, one_ingredient.price]
            actual_list.append(one_ingredient_data)

        assert actual_list == expected_list

