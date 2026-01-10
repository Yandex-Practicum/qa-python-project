from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database."""

    def test_available_buns_returns_list_of_buns(self):
        """Проверяем, что available_buns() возвращает список булочек"""
        db = Database()
        buns = db.available_buns()

        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)
        assert len(buns) == 3

    def test_available_buns_contains_correct_buns(self):
        """Проверяем содержимое списка булочек"""
        db = Database()
        buns = db.available_buns()

        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients_returns_list(self):
        """Проверяем, что available_ingredients() возвращает список"""
        db = Database()
        ingredients = db.available_ingredients()

        assert isinstance(ingredients, list)
        assert len(ingredients) == 6

    def test_available_ingredients_contains_correct_types(self):
        """Проверяем типы ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()

        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]

        assert len(sauces) == 3
        assert len(fillings) == 3

    @patch('praktikum.database.Bun')
    @patch('praktikum.database.Ingredient')
    def test_database_initialization(self, mock_ingredient, mock_bun):
        """Тестируем инициализацию базы данных с моками"""
        mock_bun.return_value = Mock()
        mock_ingredient.return_value = Mock()

        db = Database()

        assert mock_bun.call_count == 3
        assert mock_ingredient.call_count == 6
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6