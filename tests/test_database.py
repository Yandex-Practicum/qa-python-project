import pytest

from data import BUNS_DATA, FILLINGS_DATA, SAUCES_DATA, ALL_INGREDIENTS_DATA
from praktikum.database import Database


class TestDatabase:

    def test_initial_buns_count(self):
        # тест проверяет, что при инициализации база данных содержит 3 булки
        database = Database()
        assert len(database.available_buns()) == 3

    def test_initial_ingredients_count(self):
        # тест проверяет, что при инициализации база данных содержит 6 ингредиентов (3 соуса + 3 начинки)
        database = Database()
        assert len(database.available_ingredients()) == 6

    @pytest.mark.parametrize("name, price", BUNS_DATA)
    def test_available_buns(self, name, price):
        # тест проверяет, что в базе есть все булки из BUNS_DATA и каждая имеет правильную цену
        database = Database()
        buns = database.available_buns()
        names_and_prices = {bun.name: bun.price for bun in buns}
        assert names_and_prices[name] == price

    @pytest.mark.parametrize("name, price, type", ALL_INGREDIENTS_DATA)
    def test_available_ingredients(self, name, price, type):
        # тест проверяет, что в базе есть все ингредиенты и каждый имеет правильную цену
        database = Database()
        ingredients = database.available_ingredients()
        names_and_details = {ingr.name: (ingr.type, ingr.price) for ingr in ingredients}
        assert names_and_details[name][0] == type
        assert names_and_details[name][1] == price