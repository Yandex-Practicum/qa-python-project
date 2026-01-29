from ..praktikum.ingredient import Ingredient
from ..praktikum.bun import Bun


class TestDatabase:

    """Тестируем получение булочек из БД в виде списка"""
    def test_available_buns_is_list(self, database):
        assert isinstance(database.available_buns(), list)

    """Тестируем что возвращаются объекты класса Bun"""
    def test_available_buns_returns_instances_of_buns(self, database):
        assert isinstance(database.available_buns()[0], Bun)

    """Тестируем получение ингредиентов из БД в виде списка"""
    def test_available_ingredients_is_list(self, database):
        assert isinstance(database.available_ingredients(), list)

    """Тестируем что возвращаются объекты класса Ingredient"""
    def test_available_ingredients_returns_instances_of_ingredients(self, database):
        assert isinstance(database.available_ingredients()[0], Ingredient)
