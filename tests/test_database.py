import pytest
from ..database import Database
from ..bun import Bun
from ..ingredient import Ingredient
from ..ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    """Тесты для класса Database"""

    def test_database_initialization_creates_buns(self):
        """При инициализации базы данных создаются булочки"""

        db = Database()
        
        assert len(db.buns) == 3

    def test_database_initialization_creates_ingredients(self):
        """При инициализации базы данных создаются ингредиенты"""

        db = Database()
        
        assert len(db.ingredients) == 6

    def test_available_buns_return_correct_list(self):
        """Проверяет, что метод available_buns возвращает корректный список булочек"""

        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert buns == db.buns

    def test_available_ingredients_returns_correct_list(self):
        """Проверяет, что метод available_ingredients возвращает корректный список ингредиентов"""

        db = Database()
        
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert ingredients == db.ingredients

