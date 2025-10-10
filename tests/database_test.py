import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.test_data import (
    EXPECTED_BUNS_COUNT, EXPECTED_INGREDIENTS_COUNT,
    EXPECTED_SAUCE_INGREDIENTS_COUNT, EXPECTED_FILLING_INGREDIENTS_COUNT
)


class TestDatabase:
    """Тесты для класса Database"""

    def test_database_creation(self):
        """Тест создания объекта базы данных"""
        database = Database()
        
        assert len(database.buns) == EXPECTED_BUNS_COUNT
        assert len(database.ingredients) == EXPECTED_INGREDIENTS_COUNT

    def test_available_buns(self):
        """Тест метода available_buns"""
        database = Database()
        
        result = database.available_buns()
        
        assert len(result) == EXPECTED_BUNS_COUNT
        assert result == database.buns

    def test_available_ingredients(self):
        """Тест метода available_ingredients"""
        database = Database()
        
        result = database.available_ingredients()
        
        assert len(result) == EXPECTED_INGREDIENTS_COUNT
        assert result == database.ingredients

    def test_buns_data(self):
        """Тест данных булочек в базе"""
        database = Database()
        buns = database.available_buns()
        
        # Проверяем, что все булочки имеют правильную структуру
        for bun in buns:
            assert hasattr(bun, 'name')
            assert hasattr(bun, 'price')
            assert hasattr(bun, 'get_name')
            assert hasattr(bun, 'get_price')
            assert isinstance(bun.name, str)
            assert isinstance(bun.price, (int, float))

    def test_ingredients_data(self):
        """Тест данных ингредиентов в базе"""
        database = Database()
        ingredients = database.available_ingredients()
        
        # Проверяем, что все ингредиенты имеют правильную структуру
        for ingredient in ingredients:
            assert hasattr(ingredient, 'type')
            assert hasattr(ingredient, 'name')
            assert hasattr(ingredient, 'price')
            assert hasattr(ingredient, 'get_type')
            assert hasattr(ingredient, 'get_name')
            assert hasattr(ingredient, 'get_price')
            assert isinstance(ingredient.type, str)
            assert isinstance(ingredient.name, str)
            assert isinstance(ingredient.price, (int, float))

    def test_sauce_ingredients_count(self):
        """Тест количества соусов в базе"""
        database = Database()
        ingredients = database.available_ingredients()
        
        sauce_count = sum(1 for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_SAUCE)
        
        assert sauce_count == EXPECTED_SAUCE_INGREDIENTS_COUNT

    def test_filling_ingredients_count(self):
        """Тест количества начинок в базе"""
        database = Database()
        ingredients = database.available_ingredients()
        
        filling_count = sum(1 for ingredient in ingredients if ingredient.get_type() == INGREDIENT_TYPE_FILLING)
        
        assert filling_count == EXPECTED_FILLING_INGREDIENTS_COUNT

    def test_ingredient_types(self):
        """Тест типов ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()
        
        for ingredient in ingredients:
            ingredient_type = ingredient.get_type()
            assert ingredient_type in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]

    def test_database_with_fixture(self, database):
        assert len(database.available_buns()) == EXPECTED_BUNS_COUNT
        assert len(database.available_ingredients()) == EXPECTED_INGREDIENTS_COUNT 