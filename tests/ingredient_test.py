import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type,expected_type", [
        (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_FILLING),
        ("UNKNOWN_TYPE", "UNKNOWN_TYPE")
    ])
    def test_get_type_returns_correct_value_for_different_types(self, ingredient_type, expected_type):
        ingredient = Ingredient(ingredient_type, "test", 100.0)
        
        result = ingredient.get_type()
        
        assert result == expected_type
    
    @pytest.mark.parametrize("name,expected_name", [
        ("hot sauce", "hot sauce"),
        ("sour cream", "sour cream"),
        ("cutlet", "cutlet"),
        ("dinosaur", "dinosaur"),
        ("", "")
    ])
    def test_get_name_returns_correct_value_for_different_names(self, name, expected_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100.0)
        
        result = ingredient.get_name()
        
        assert result == expected_name
    
    @pytest.mark.parametrize("price,expected_price", [
        (100.0, 100.0),
        (200.0, 200.0),
        (300.0, 300.0),
        (0.0, 0.0),
        (999.99, 999.99)
    ])
    def test_get_price_returns_correct_value_for_different_prices(self, price, expected_price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", price)
        
        result = ingredient.get_price()
        
        assert result == expected_price
    
    def test_ingredient_creation_sets_type_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
    
    def test_ingredient_creation_sets_name_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        
        assert ingredient.name == "hot sauce"
    
    def test_ingredient_creation_sets_price_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        
        assert ingredient.price == 100.0
    
    def test_mock_ingredient_get_type_returns_mocked_value(self):
        mock_ingredient = Mock(spec=Ingredient)
        expected_type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_type.return_value = expected_type
        
        result = mock_ingredient.get_type()
        
        assert result == expected_type
        mock_ingredient.get_type.assert_called_once()
    
    def test_mock_ingredient_get_name_returns_mocked_value(self):
        mock_ingredient = Mock(spec=Ingredient)
        expected_name = "mock sauce"
        mock_ingredient.get_name.return_value = expected_name
        
        result = mock_ingredient.get_name()
        
        assert result == expected_name
        mock_ingredient.get_name.assert_called_once()
    
    def test_mock_ingredient_get_price_returns_mocked_value(self):
        mock_ingredient = Mock(spec=Ingredient)
        expected_price = 300.0
        mock_ingredient.get_price.return_value = expected_price
        
        result = mock_ingredient.get_price()
        
        assert result == expected_price
        mock_ingredient.get_price.assert_called_once()