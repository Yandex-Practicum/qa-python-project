import pytest
from praktikum.database import Database
from data import data
from unittest.mock import Mock 


class TestDatabase:
    def test_create_bun_in_database(self, database):
        mock_bun = Mock()
        mock_bun.name = data.bun_name
        mock_bun.price = data.bun_price
        database.buns = [mock_bun]
        bun_list = [[bun.name, bun.price] for bun in database.buns]
        assert bun_list == [[data.bun_name,data.bun_price]]

    @pytest.mark.parametrize(
        "ingredient_type, ingredient_value",
        [("SAUCE", data.sauce_names_in_dtb), ("FILLING", data.filling_names_in_dtb)],
    )
    def test_create_ingredient_in_database(self, database, ingredient_type, ingredient_value):
        mock_ingredients = []
        for value in ingredient_value:
            mock_ingredient = Mock()
            mock_ingredient.name = value[0] 
            mock_ingredient.price = value[2]
            mock_ingredient.type = ingredient_type  
            mock_ingredients.append(mock_ingredient)

        database.ingredients = mock_ingredients
        ingredient = list(filter(lambda x: x.type == ingredient_type, database.ingredients))
        ingredient_names = [[ingredient.name, ingredient.type, ingredient.price] for ingredient in ingredient]
        assert ingredient_names == ingredient_value
 

    def test_available_buns(self,database):
        mock_bun = Mock()
        mock_bun.name = data.bun_name
        mock_bun.price = data.bun_price
        database.buns = [mock_bun]
        buns = database.available_buns()
        buns_list = [[bun.name, bun.price] for bun in buns]
        assert buns_list == [[data.bun_name,data.bun_price]]

    def test_available_ingredients(self,database):
        mock_ingredient = Mock()
        mock_ingredient.name = data.ingredient_name
        mock_ingredient.price = data.ingredient_price
        mock_ingredient.type = data.ingredient_type
        database.ingredients = [mock_ingredient]
        ingredients = database.available_ingredients()
        ingredients_list = [[ingredient.type, ingredient.name, ingredient.price] for ingredient in ingredients]
        assert ingredients_list == [[data.ingredient_type, data.ingredient_name,  data.ingredient_price]]