from data import buns_generator, ingredients_generator
from praktikum.database import Database
from praktikum.ingredient_types import *


class TestDataBase:
    def test_data_base_get_buns(self, db):
        mock_buns = buns_generator()
        buns = db.available_buns()
        for i in range(3):
            bun = buns[i]
            mock_bun = mock_buns[i]

            assert bun.get_name() == mock_bun.get_name() and bun.get_price() == mock_bun.get_price()

    def test_data_base_get_ingredients(self, db):
        mock_ingredients = ingredients_generator(INGREDIENT_TYPE_SAUCE) + ingredients_generator(INGREDIENT_TYPE_FILLING)
        ingredients = db.available_ingredients()
        for i in range(6):
            mock_ingredient = mock_ingredients[i]
            ingredient = ingredients[i]

            assert (
                ingredient.get_type() == mock_ingredient.get_type() and
                ingredient.get_name() == mock_ingredient.get_name() and
                ingredient.get_price() == mock_ingredient.get_price()
            )
