import pytest
from unittest.mock import Mock, patch
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
   

    def setup_method(self):
        self.database = Database()

    def test_init(self):
        assert len(self.database.buns) == 3
        assert len(self.database.ingredients) == 6

    def test_available_buns(self):
        buns = self.database.available_buns()
        
        assert len(buns) == 3
        assert isinstance(buns[0], Bun)
        assert buns[0].get_name() == "black bun"
        assert buns[0].get_price() == 100
        
        assert buns[1].get_name() == "white bun"
        assert buns[1].get_price() == 200
        
        assert buns[2].get_name() == "red bun"
        assert buns[2].get_price() == 300

    def test_available_ingredients(self):
        ingredients = self.database.available_ingredients()
        
        assert len(ingredients) == 6
        assert isinstance(ingredients[0], Ingredient)
        
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[0].get_name() == "hot sauce"
        assert ingredients[0].get_price() == 100
        
        assert ingredients[1].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[1].get_name() == "sour cream"
        assert ingredients[1].get_price() == 200
        
        assert ingredients[2].get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredients[2].get_name() == "chili sauce"
        assert ingredients[2].get_price() == 300
        
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[3].get_name() == "cutlet"
        assert ingredients[3].get_price() == 100
        
        assert ingredients[4].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[4].get_name() == "dinosaur"
        assert ingredients[4].get_price() == 200
        
        assert ingredients[5].get_type() == INGREDIENT_TYPE_FILLING
        assert ingredients[5].get_name() == "sausage"
        assert ingredients[5].get_price() == 300

    def test_buns_list_is_mutable(self):
      
        buns = self.database.available_buns()
        original_count = len(buns)
        
        new_bun = Bun("test bun", 400)
        buns.append(new_bun)
        
        assert len(self.database.buns) == original_count + 1
        assert self.database.buns[-1].get_name() == "test bun"

    def test_ingredients_list_is_mutable(self):
        ingredients = self.database.available_ingredients()
        original_count = len(ingredients)
        
        new_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 400)
        ingredients.append(new_ingredient)
        
        assert len(self.database.ingredients) == original_count + 1
        assert self.database.ingredients[-1].get_name() == "test sauce"