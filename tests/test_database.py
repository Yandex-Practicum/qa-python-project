import pytest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from database import Database


@pytest.fixture
def database():
    """Фикстура для создания базы данных"""
    return Database()


class TestDatabase:
    """Тесты для класса Database"""
    
    def test_database_initialization(self, database):
        """Только инициализация"""
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        
        assert len(buns) == 3
        assert len(ingredients) == 6
    
    def test_available_buns(self, database):
        """Только получение булочек"""
        buns = database.available_buns()
        
        assert len(buns) == 3
        # ИСПРАВЛЕНИЕ: заменили "in" на точное сравнение
        bun_names = [bun.get_name() for bun in buns]
        assert bun_names == ["black bun", "white bun", "red bun"]
    
    def test_available_ingredients(self, database):
        """Только получение ингредиентов"""
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6