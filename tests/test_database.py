import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    def setup_method(self):
        self.database = Database()
    
    def test_available_buns_returns_list_of_buns(self):
        """Тестируем, что available_buns возвращает список булочек"""
        buns = self.database.available_buns()
        assert isinstance(buns, list)
        assert len(buns) > 0
        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_ingredients_returns_list_of_ingredients(self):
        """Тестируем, что available_ingredients возвращает список ингредиентов"""
        ingredients = self.database.available_ingredients()
        assert isinstance(ingredients, list)
        assert len(ingredients) > 0
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    
    def test_database_initialization_creates_buns(self):
        """Тестируем, что при инициализации создаются булочки"""
        buns = self.database.buns
        assert len(buns) == 3
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300
    
    def test_database_initialization_creates_ingredients(self):
        """Тестируем, что при инициализации создаются ингредиенты"""
        ingredients = self.database.ingredients
        assert len(ingredients) == 6
        # Проверяем соусы
        assert ingredients[0].get_type() == "SAUCE"
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        
        assert ingredients[1].get_type() == "SAUCE"
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        
        assert ingredients[2].get_type() == "SAUCE"
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300
        
        # Проверяем начинки
        assert ingredients[3].get_type() == "FILLING"
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        
        assert ingredients[4].get_type() == "FILLING"
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200
        
        assert ingredients[5].get_type() == "FILLING"
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300