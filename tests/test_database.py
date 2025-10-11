import data
from praktikum.database import Database


class TestDatabase:

    def test_default_bun(self):
        database = Database()

        for i in range(len(data.database_buns)):
            assert data.database_buns[i][0] == database.available_buns()[i].name
            assert data.database_buns[i][1] == database.available_buns()[i].price

    def test_default_ingredients(self):
        database = Database()

        for i in range(len(data.database_ingredients)):
            assert data.database_ingredients[i][0] == database.available_ingredients()[i].type
            assert data.database_ingredients[i][1] == database.available_ingredients()[i].name
            assert data.database_ingredients[i][2] == database.available_ingredients()[i].price
