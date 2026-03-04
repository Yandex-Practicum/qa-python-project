import pytest
from unittest.mock import Mock, patch, MagicMock
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    
    def setup_method(self):
        #Подготовка данных перед каждым тестом
        self.db = Database()
    
    def test_database_initialization(self):
        #Проверка инициализации базы данных
        assert hasattr(self.db, 'buns')
        assert hasattr(self.db, 'ingredients')
        assert len(self.db.buns) > 0
        assert len(self.db.ingredients) > 0
    
    def test_available_buns(self):
        #Проверка получения списка булочек
        buns = self.db.available_buns()
        assert isinstance(buns, list)
        assert len(buns) == len(self.db.buns)
        for bun in buns:
            assert isinstance(bun, Bun)
    
    def test_available_ingredients(self):
        #Проверка получения списка ингредиентов
        ingredients = self.db.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) == len(self.db.ingredients)
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
    
    def test_available_ingredients_invalid_type(self):
        #Проверка получения всех ингредиентов (метод не фильтрует по типу)
        ingredients = self.db.available_ingredients()
    
        # Проверяем, что возвращаются все ингредиенты
        assert isinstance(ingredients, list)
        assert len(ingredients) == len(self.db.ingredients)
    
        # Проверяем, что среди ингредиентов есть и соусы, и начинки
        has_sauce = False
        has_filling = False
    
        for ingredient in ingredients:
            if ingredient.get_type() == INGREDIENT_TYPE_SAUCE:
                has_sauce = True
            elif ingredient.get_type() == INGREDIENT_TYPE_FILLING:
                has_filling = True
    
        assert has_sauce and has_filling
    
    @patch('praktikum.database.Database.available_buns')
    def test_database_methods_callable(self, mock_available_buns):
        #Проверка, что методы базы данных вызываются корректно
        mock_available_buns.return_value = ["mock_bun1", "mock_bun2"]
        
        result = self.db.available_buns()
        
        mock_available_buns.assert_called_once()
        assert result == ["mock_bun1", "mock_bun2"]
    
    def test_database_data_integrity(self):
        #Проверка целостности данных в базе
        # Проверяем булочки
        for bun in self.db.buns:
            assert isinstance(bun.get_name(), str)
            assert isinstance(bun.get_price(), (int, float))
            assert bun.get_price() > 0
        
        # Проверяем ингредиенты
        for ingredient in self.db.ingredients:
            assert ingredient.get_type() in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]
            assert isinstance(ingredient.get_name(), str)
            assert isinstance(ingredient.get_price(), (int, float))
            assert ingredient.get_price() > 0