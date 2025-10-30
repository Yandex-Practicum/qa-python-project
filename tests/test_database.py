import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def setup_method(self):
        self.database = Database()
    
    def test_available_buns(self):
        buns = self.database.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        
        # Проверяем корректные названия булок
        bun_names = [bun.get_name() for bun in buns]
        expected_bun_names = ["black bun", "white bun", "red bun"]
        
        for expected_name in expected_bun_names:
            assert any(expected_name in bun.get_name().lower() for bun in buns)
    
    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        # Проверяем соусы
        sauces = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        
        sauce_names = [sauce.get_name() for sauce in sauces]
        expected_sauce_names = ["hot sauce", "sour cream", "chili sauce"]
        
        for expected_name in expected_sauce_names:
            assert any(expected_name in sauce.get_name().lower() for sauce in sauces)
        
        # Проверяем начинки
        fillings = [ing for ing in ingredients if ing.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        
        filling_names = [filling.get_name() for filling in fillings]
        expected_filling_names = ["cutlet", "dinosaur", "sausage"]
        
        for expected_name in expected_filling_names:
            assert any(expected_name in filling.get_name().lower() for filling in fillings)
    
    def test_ingredient_prices(self):
        ingredients = self.database.available_ingredients()
        
        prices = [ing.get_price() for ing in ingredients]
        expected_prices = [100, 200, 300, 100, 200, 300]
        
        assert sorted(prices) == sorted(expected_prices)
    
    def test_database_with_russian_ingredients(self):
        database = Database()
        buns = database.available_buns()
        ingredients = database.available_ingredients()
        
        assert len(buns) > 0
        assert len(ingredients) > 0
        
        for bun in buns:
            assert bun.get_price() >= 0
        
        for ingredient in ingredients:
            assert ingredient.get_price() >= 0