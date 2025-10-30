import pytest
from praktikum.database import Database
from data import data


class TestDatabase:
    def test_create_bun_in_database(self, database):
        bun_list = [[bun.name, bun.price] for bun in database.buns]
        assert bun_list == data.bun_list

    @pytest.mark.parametrize(
        "ingredient_type, ingredient_value",
        [("SAUCE", data.sauce_names_in_dtb), ("FILLING", data.filling_names_in_dtb)],
    )
    def test_create_ingredient_in_database(self, database, ingredient_type, ingredient_value):
        database = Database()
        ingredient = list(
            filter(lambda x: x.type == ingredient_type, database.ingredients)
        )
        ingredient_names = [[ingredient.name, ingredient.type, ingredient.price] for ingredient in ingredient]
        assert ingredient_names == ingredient_value

    def test_available_buns(self,database):
        buns = database.available_buns()
        buns_list = [[bun.name, bun.price] for bun in buns]
        assert buns_list == data.bun_list

    def test_available_ingredients(self,database):
        ingredients = database.available_ingredients()
        ingredients_list = [[ingredient.name, ingredient.type, ingredient.price] for ingredient in ingredients]
        assert ingredients_list == data.ingredients_list
        
    

