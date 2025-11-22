from data import Data
from praktikum.database import Database


class TestDatabase:

    def test_database_available_buns_check(self):
        buns = []
        for bun in Database().available_buns():
            buns.append((bun.name, bun.price))
        assert buns == Data.DB_BUNS

    def test_database_available_ingredients_check(self):
        ingredients = []
        for ingredient in Database().available_ingredients():
            ingredients.append((ingredient.type, ingredient.name, ingredient.price))
        assert ingredients == Data.DB_INGREDIENTS
