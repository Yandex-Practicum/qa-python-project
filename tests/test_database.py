"""
Тесты для класса Database из database.py
"""
import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тестирование базы данных"""

    def test_database_initialization(self):
        """Проверка инициализации базы данных"""
    
        database = Database()

        
        # Проверяем количество булочек
        assert len(database.buns) == 3
        # Проверяем количество ингредиентов (3 соуса + 3 начинки)
        assert len(database.ingredients) == 6

    def test_available_buns(self):
        """Проверка получения списка доступных булочек"""
       
        database = Database()

        buns = database.available_buns()

        assert isinstance(buns, list)
        assert len(buns) == 3
        
        # Проверяем, что все элементы - объекты Bun
        for bun in buns:
            assert isinstance(bun, Bun)
        
        # Проверяем названия булочек
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names

    def test_available_ingredients(self):
        """Проверка получения списка доступных ингредиентов"""
        
        database = Database()

       
        ingredients = database.available_ingredients()

        
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        
        # Проверяем, что все элементы - объекты Ingredient
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
        
        # Проверяем типы ингредиентов
        ingredient_types = [ingredient.get_type() for ingredient in ingredients]
        assert ingredient_types.count(INGREDIENT_TYPE_SAUCE) == 3
        assert ingredient_types.count(INGREDIENT_TYPE_FILLING) == 3

    def test_bun_prices(self):
        """Проверка цен булочек в базе данных"""
        
        database = Database()

       
        buns = database.available_buns()

       
        prices = [bun.get_price() for bun in buns]
        assert 100.0 in prices  # black bun
        assert 200.0 in prices  # white bun
        assert 300.0 in prices  # red bun

    def test_ingredient_names(self):
        """Проверка названий ингредиентов в базе данных"""
        
        database = Database()

        
        ingredients = database.available_ingredients()
        ingredient_names = [ingredient.get_name() for ingredient in ingredients]

        #  для соусов
        assert "hot sauce" in ingredient_names
        assert "sour cream" in ingredient_names
        assert "chili sauce" in ingredient_names
        
        #  для начинок
        assert "cutlet" in ingredient_names
        assert "dinosaur" in ingredient_names
        assert "sausage" in ingredient_names
