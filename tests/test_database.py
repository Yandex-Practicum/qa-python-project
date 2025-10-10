from praktikum.bun import Bun
from tests.conftest import TEST_BUNS, TEST_INGREDIENTS


class TestDatabase:
    def test_database_constructor(self, create_database):
        actual_buns = [(bun.name, bun.price) for bun in create_database.buns]
        expected_buns = [(bun.name, bun.price) for bun in TEST_BUNS]
        actual_ingredients = [(ingredient.name, ingredient.price) for ingredient in create_database.ingredients]
        expected_ingredients = [(ingredient.name, ingredient.price) for ingredient in TEST_INGREDIENTS]
        assert actual_buns == expected_buns and actual_ingredients == expected_ingredients

    def test_available_buns(self, create_database):
        assert create_database.available_buns() == create_database.buns

    def test_available_ingredients(self, create_database):
        assert create_database.available_ingredients() == create_database.ingredients
