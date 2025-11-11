import pytest
from unittest.mock import patch, Mock
from praktikum.database import Database


class TestDatabase:

    def test_available_buns_returns_list_of_buns(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) > 0
        for bun in buns:
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')
            assert callable(bun.get_name)
            assert callable(bun.get_price)

    def test_available_ingredients_returns_list_of_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
        for ingredient in ingredients:
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_price')
            assert hasattr(ingredient, 'get_type')
            assert callable(ingredient.get_name)
            assert callable(ingredient.get_price)
            assert callable(ingredient.get_type)

    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization_creates_objects(self, mock_ingredient, mock_bun):
        db = Database()
        
        assert mock_bun.called
        assert mock_ingredient.called

    def test_available_methods_return_non_empty_lists(self):
        db = Database()
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        
        assert len(buns) > 0
        assert len(ingredients) > 0