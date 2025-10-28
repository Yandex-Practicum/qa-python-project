import pytest
from unittest.mock import patch, Mock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import (
    EXPECTED_BUNS_COUNT,
    EXPECTED_INGREDIENTS_COUNT,
    BUN_NAMES,
    INGREDIENT_PRICES,
)


class TestDatabase:
    """Тестовый класс для базы данных."""

    def test_database_initialization_creates_buns_and_ingredients(self):
        """Тест инициализации создает булочки и ингредиенты."""
        db = Database()
        
        assert len(db.buns) == EXPECTED_BUNS_COUNT
        assert len(db.ingredients) == EXPECTED_INGREDIENTS_COUNT

    def test_available_buns_returns_all_buns(self):
        """Тест available_buns возвращает все булочки."""
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == EXPECTED_BUNS_COUNT
        assert all(isinstance(bun, Bun) for bun in buns)
        
        bun_names = [bun.get_name() for bun in buns]
        for name in BUN_NAMES:
            assert name in bun_names

    def test_available_ingredients_returns_all_ingredients(self):
        """Тест available_ingredients возвращает все ингредиенты."""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == EXPECTED_INGREDIENTS_COUNT
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        ingredient_types = [ingredient.get_type() for ingredient in ingredients]
        assert INGREDIENT_TYPE_SAUCE in ingredient_types
        assert INGREDIENT_TYPE_FILLING in ingredient_types

    def test_ingredients_have_correct_prices(self):
        """Тест ингредиенты имеют корректные цены."""
        db = Database()
        ingredients = db.available_ingredients()
        
        prices = [ingredient.get_price() for ingredient in ingredients]
        assert all(price in INGREDIENT_PRICES for price in prices)

    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization_with_mocks(self, MockIngredient, MockBun):
        """Тест инициализации базы данных с моками."""
        mock_bun = Mock()
        mock_ingredient = Mock()
        
        MockBun.return_value = mock_bun
        MockIngredient.return_value = mock_ingredient
        
        db = Database()
        
        assert MockBun.call_count == EXPECTED_BUNS_COUNT
        assert MockIngredient.call_count == EXPECTED_INGREDIENTS_COUNT
        
        buns = db.available_buns()
        ingredients = db.available_ingredients()
        
        assert len(buns) == EXPECTED_BUNS_COUNT
        assert len(ingredients) == EXPECTED_INGREDIENTS_COUNT
