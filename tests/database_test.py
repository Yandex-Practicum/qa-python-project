import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import Mock, patch
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:
    
    def test_database_initialization_creates_three_buns(self):
        database = Database()
        
        assert len(database.buns) == 3
    
    def test_database_initialization_creates_six_ingredients(self):
        database = Database()
        
        assert len(database.ingredients) == 6
    
    def test_first_bun_has_correct_name(self):
        database = Database()
        
        assert database.buns[0].name == "black bun"
    
    def test_first_bun_has_correct_price(self):
        database = Database()
        
        assert database.buns[0].price == 100.0
    
    def test_second_bun_has_correct_name(self):
        database = Database()
        
        assert database.buns[1].name == "white bun"
    
    def test_third_bun_has_correct_name(self):
        database = Database()
        
        assert database.buns[2].name == "red bun"
    
    def test_first_ingredient_is_sauce_type(self):
        database = Database()
        
        assert database.ingredients[0].type == INGREDIENT_TYPE_SAUCE
    
    def test_first_ingredient_has_correct_name(self):
        database = Database()
        
        assert database.ingredients[0].name == "hot sauce"
    
    def test_fourth_ingredient_is_filling_type(self):
        database = Database()
        
        assert database.ingredients[3].type == INGREDIENT_TYPE_FILLING
    
    def test_fourth_ingredient_has_correct_name(self):
        database = Database()
        
        assert database.ingredients[3].name == "cutlet"
    
    def test_available_buns_returns_list_of_buns(self):
        database = Database()
        
        buns = database.available_buns()
        
        assert isinstance(buns, list)
        assert len(buns) == 3
        assert all(isinstance(bun, Bun) for bun in buns)
    
    def test_available_buns_returns_correct_number_of_buns(self):
        database = Database()
        
        buns = database.available_buns()
        
        assert len(buns) == 3
    
    def test_available_ingredients_returns_list_of_ingredients(self):
        database = Database()
        
        ingredients = database.available_ingredients()
        
        assert isinstance(ingredients, list)
        assert len(ingredients) == 6
        assert all(isinstance(ingredient, Ingredient) for ingredient in ingredients)
    
    def test_available_ingredients_returns_correct_number_of_ingredients(self):
        database = Database()
        
        ingredients = database.available_ingredients()
        
        assert len(ingredients) == 6
    
    @patch('praktikum.database.Bun')
    def test_database_creates_buns_using_bun_class(self, mock_bun_class):
        mock_bun = Mock()
        mock_bun_class.return_value = mock_bun
        
        with patch('praktikum.database.Bun', mock_bun_class):
            database = Database()
        
        assert mock_bun_class.call_count == 3
    
    @patch('praktikum.database.Ingredient')
    def test_database_creates_ingredients_using_ingredient_class(self, mock_ingredient_class):
        mock_ingredient = Mock()
        mock_ingredient_class.return_value = mock_ingredient
        
        with patch('praktikum.database.Ingredient', mock_ingredient_class):
            database = Database()
        
        assert mock_ingredient_class.call_count == 6
    
    def test_database_instances_are_independent(self):
        db1 = Database()
        db2 = Database()
        
        assert db1 is not db2
        assert db1.buns is not db2.buns
        assert db1.ingredients is not db2.ingredients