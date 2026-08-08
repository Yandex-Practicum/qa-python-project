import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import BunTestData, IngredientTestData


class TestDatabase:
    
    def test_database_initialization(self, db):
        
        assert len(db.buns) == 3
        assert len(db.ingredients) == 6

    def test_available_buns(self, db):
        
        buns = db.available_buns()
        
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
        
    
        for bun in buns:
            assert bun.get_name() is not None
            assert bun.get_price() is not None

    def test_available_ingredients(self, db):
        
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
        
        
        sauces = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3
        for sauce in sauces:
            assert sauce.get_name() is not None
            assert sauce.get_price() is not None
    
        fillings = [i for i in ingredients if i.get_type() == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3
        for filling in fillings:
            assert filling.get_name() is not None
            assert filling.get_price() is not None

    def test_database_buns_are_different_objects(self, db):
        
        buns = db.available_buns()
        assert buns[0] is not buns[1]
        assert buns[1] is not buns[2]

    def test_database_ingredients_are_different_objects(self, db):
        
        ingredients = db.available_ingredients()
        for i in range(len(ingredients) - 1):
            assert ingredients[i] is not ingredients[i + 1]