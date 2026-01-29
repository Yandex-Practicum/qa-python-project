import pytest
from praktikum.database import Database
from data_tests import database_test_data


class TestDatabase:
    @pytest.mark.parametrize("buns_count, ingredients_count", database_test_data)
    def test_available_buns(self, buns_count, ingredients_count, mock_bun):
        mock_buns = [mock_bun for _ in range(buns_count)]
        database = Database()
        database.buns = mock_buns
        assert len(database.available_buns()) == buns_count

    @pytest.mark.parametrize("buns_count, ingredients_count", database_test_data)
    def test_available_ingredients(self, buns_count, ingredients_count, mock_ingredient):
        mock_ingredients = [mock_ingredient for _ in range(ingredients_count)]
        database = Database()
        database.ingredients = mock_ingredients
        assert len(database.available_ingredients()) == ingredients_count