import pytest
from unittest.mock import patch, MagicMock
from praktikum.database import Database

class TestDatabase:
    # Тесты для available_buns()
    def test_available_buns_returns_list(self):
        """Проверяем, что available_buns() возвращает список"""
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_available_buns_returns_three_buns(self):
        """Проверяем, что available_buns() возвращает 3 булочки"""
        db = Database()
        assert len(db.available_buns()) == 3

    # Тесты для available_ingredients()
    def test_available_ingredients_returns_list(self):
        """Проверяем, что available_ingredients() возвращает список"""
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_available_ingredients_returns_six_items(self):
        """Проверяем, что available_ingredients() возвращает 6 ингредиентов"""
        db = Database()
        assert len(db.available_ingredients()) == 6

    def test_available_ingredients_has_three_sauces(self):
        """Проверяем количество соусов"""
        db = Database()
        sauces = [i for i in db.available_ingredients() if i.get_type() == "SAUCE"]
        assert len(sauces) == 3

    # Тесты с моками
    @patch('praktikum.database.Bun')
    def test_init_creates_three_buns(self, mock_bun):
        """Проверяем создание 3 булочек при инициализации"""
        Database()
        assert mock_bun.call_count == 3

    @patch('praktikum.database.Ingredient')
    def test_init_creates_six_ingredients(self, mock_ingredient):
        """Проверяем создание 6 ингредиентов при инициализации"""
        Database()
        assert mock_ingredient.call_count == 6