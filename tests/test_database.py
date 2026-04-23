import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


class TestDatabase:
    
    def test_available_buns_returns_list(self):
        """Тест: available_buns возвращает список булок"""
        db = Database()
        buns = db.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) == 3
        for bun in buns:
            assert isinstance(bun, Bun)
    
    def test_available_buns_contains_expected_buns(self):
        """Тест: проверка содержимого списка булок"""
        db = Database()
        buns = db.available_buns()
        
        bun_names = [bun.get_name() for bun in buns]
        bun_prices = [bun.get_price() for bun in buns]
        
        assert "black bun" in bun_names
        assert "white bun" in bun_names
        assert "red bun" in bun_names
        assert 100 in bun_prices
        assert 200 in bun_prices
        assert 300 in bun_prices
    
    def test_available_ingredients_returns_list(self):
        """Тест: available_ingredients возвращает список ингредиентов"""
        db = Database()
        ingredients = db.available_ingredients()
        
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        for ingredient in ingredients:
            assert isinstance(ingredient, Ingredient)
    
    def test_available_ingredients_contains_expected_count(self):
        """Тест: проверка количества соусов и начинок"""
        db = Database()
        ingredients = db.available_ingredients()
        
        sauces = [ing for ing in ingredients if ing.get_type() == "SAUCE"]
        fillings = [ing for ing in ingredients if ing.get_type() == "FILLING"]
        
        assert len(sauces) == 3
        assert len(fillings) == 3