"""Тесты для класса Database"""
import pytest
from tests.test_data import TEST_BUNS, TEST_INGREDIENTS


class TestDatabase:
    """Тестовый класс для проверки класса Database"""
    
    def test_available_buns_returns_all_buns(self, database):
        """Тест метода available_buns - проверяем только этот метод"""
        buns = database.available_buns()        
  
        assert len(buns) == 3
    
    def test_available_ingredients_returns_all_ingredients(self, database):
        """Тест метода available_ingredients - проверяем только этот метод"""
        ingredients = database.available_ingredients()        

        assert len(ingredients) == 6
    
    def test_available_buns_returns_bun_objects(self, database):
        """Тест что available_buns возвращает объекты Bun"""
        from praktikum.bun import Bun
        buns = database.available_buns()        

        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_ingredients_returns_ingredient_objects(self, database):
        """Тест что available_ingredients возвращает объекты Ingredient"""
        from praktikum.ingredient import Ingredient
        ingredients = database.available_ingredients()        

        assert all(isinstance(ing, Ingredient) for ing in ingredients)
    
    def test_buns_have_correct_data(self, database):
        """Тест данных булочек - прямой доступ к атрибуту buns"""

        bun_names = [bun.get_name() for bun in database.buns]
        assert bun_names == ["black bun", "white bun", "red bun"]
    
    def test_ingredients_have_correct_types(self, database):
        """Тест типов ингредиентов - прямой доступ к атрибуту ingredients"""

        ingredient_types = [ing.get_type() for ing in database.ingredients]
        
        assert "SAUCE" in ingredient_types and "FILLING" in ingredient_types