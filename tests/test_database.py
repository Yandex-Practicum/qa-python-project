import pytest
from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_database_initialization(self):
        db = Database()
        
        buns = db.available_buns()
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    
    def test_available_buns_returns_correct_buns(self):
        db = Database()
        buns = db.available_buns()
        
        bun_names = [bun.get_name() for bun in buns]
        assert "black bun" in bun_names
        assert "white bun" in bun_names  
        assert "red bun" in bun_names