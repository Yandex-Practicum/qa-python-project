import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) > 0

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0

    def test_buns_have_name_and_price(self):
        db = Database()
        buns = db.available_buns()

        for bun in buns:
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')
            assert isinstance(bun.get_name(), str)
            assert isinstance(bun.get_price(), float)

    def test_ingredients_have_type_name_and_price(self):
        db = Database()
        ingredients = db.available_ingredients()

        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_type')
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_price')
            assert isinstance(ingredient.get_name(), str)
            assert isinstance(ingredient.get_price(), float)

    def test_database_initialization(self):
        db = Database()
        assert hasattr(db, 'buns')
        assert hasattr(db, 'ingredients')

    @patch('praktikum.database.Database._init_buns')
    @patch('praktikum.database.Database._init_ingredients')
    def test_database_constructor_calls_init_methods(self, mock_init_ingredients, mock_init_buns):
        Database()
        mock_init_buns.assert_called_once()
        mock_init_ingredients.assert_called_once()
