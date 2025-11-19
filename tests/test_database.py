import pytest
from unittest.mock import patch
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    """Тест-кейсы для класса Database"""
    
    # 1. Тест получения списка булочек
    def test_available_buns_when_called_then_returns_buns_list(self, database, mock_bun):
        """1. Метод available_buns() возвращает список булочек"""
        database.buns = [mock_bun]
        buns = database.available_buns()
        assert len(buns) == 1
    
    # 2. Тест получения списка ингредиентов
    def test_available_ingredients_when_called_then_returns_ingredients_list(self, database, mock_ingredient):
        """2. Метод available_ingredients() возвращает список ингредиентов"""
        database.ingredients = [mock_ingredient]
        ingredients = database.available_ingredients()
        assert len(ingredients) == 1
    
    # 3. Тест загрузки начальных данных
    @patch('praktikum.database.Database.load_initial_data')
    def test_init_when_called_then_loads_initial_data(self, mock_load):
        """3. При инициализации загружаются начальные данные"""
        from praktikum.database import Database
        Database()
        mock_load.assert_called_once()
    
    # 4. Тест получения пустого списка булочек
    def test_available_buns_when_empty_then_returns_empty_list(self, database):
        """4. Метод available_buns() возвращает пустой список при отсутствии булочек"""
        database.buns = []
        assert len(database.available_buns()) == 0
    
    # 5. Параметризованный тест фильтрации ингредиентов по типу
    @pytest.mark.parametrize("ingredient_type,expected_count", [
        (INGREDIENT_TYPE_SAUCE, 3),
        (INGREDIENT_TYPE_FILLING, 3)
    ])
    def test_available_ingredients_when_called_then_returns_correct_types(
        self, database, ingredient_type, expected_count
    ):
        """5. Метод available_ingredients() возвращает ингредиенты нужного типа"""
        ingredients = database.available_ingredients()
        count = sum(1 for ing in ingredients if ing.get_type() == ingredient_type)
        assert count == expected_count