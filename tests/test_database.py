import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:
    """Тесты для класса Database"""

    def test_initialization_database(self):
        """Тест инициализации"""
        database = Database()
        
        assert len(database.buns) == 3
        assert len(database.ingredients) == 6


    def test_available_buns_content(self):
        """Тест содержания доступных булок"""
        database = Database()
        buns = database.available_buns()
        
        bun_names = [bun.get_name() for bun in buns]
        bun_prices = [bun.get_price() for bun in buns]
        
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names
        assert 100 in bun_prices
        assert 200 in bun_prices
        assert 300 in bun_prices

    def test_available_ingredients(self):
        """Тест получения доступных ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6

    def test_available_ingredients_content(self):
        """Тест содержания доступных ингредиентов"""
        database = Database()
        ingredients = database.available_ingredients()
        
        ing_names = [ing.get_name() for ing in ingredients]
        
        assert "hot sauce" in ing_names
        assert "sour cream" in ing_names
        assert "chili sauce" in ing_names
        assert "cutlet" in ing_names
        assert "dinosaur" in ing_names
        assert "sausage" in ing_names