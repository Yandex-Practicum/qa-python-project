import pytest
from unittest.mock import Mock, patch
from database import Database
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns(self):
        db = Database()
        buns = db.available_buns()
        
        assert len(buns) == 2
        
        assert buns[0].get_name() == "Краторная булка N-200i"
        assert buns[0].get_price() == 1255
        assert buns[1].get_name() == "Флюоресцентная булка R2-D3"
        assert buns[1].get_price() == 988

    def test_available_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()
        
        assert len(ingredients) == 11  # 2 соуса + 9 начинок
        
        
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "Соус фирменный Space Sauce"
        assert ingredients[0].get_price() == 80
        
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "Соус традиционный галактический"
        assert ingredients[1].get_price() == 15
        
        
        assert ingredients[2].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[2].get_name() == "Хрустящие минеральные кольца"
        assert ingredients[2].get_price() == 300
        
        
        assert ingredients[10].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[10].get_name() == "Биокотлета из марсианской Магнолии"
        assert ingredients[10].get_price() == 424

    def test_available_buns_returns_list(self):
        db = Database()
        buns = db.available_buns()
        assert isinstance(buns, list)
        assert all(isinstance(bun, Bun) for bun in buns)

    def test_available_ingredients_returns_list(self):
        db = Database()
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)
        assert all(isinstance(ing, Ingredient) for ing in ingredients)