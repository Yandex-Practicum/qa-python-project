"""Тесты для класса Ingredient"""
import pytest
from praktikum.ingredient import Ingredient
from tests.test_data import TEST_INGREDIENTS


class TestIngredient:
    """Тестовый класс для проверки класса Ingredient"""
    
    @pytest.mark.parametrize("test_data", [
        TEST_INGREDIENTS[0],  # SAUCE, hot sauce, 100
        TEST_INGREDIENTS[1],  # SAUCE, sour cream, 200
        TEST_INGREDIENTS[4],  # FILLING, cutlet, 100
        TEST_INGREDIENTS[5],  # FILLING, dinosaur, 200
    ])
    def test_ingredient_initialization(self, test_data):
        """Тест инициализации ингредиента с параметризацией"""
        
        ingredient = Ingredient(test_data["type"], test_data["name"], test_data["price"])
        
        
        assert ingredient.type == test_data["type"]
        assert ingredient.name == test_data["name"]
        assert ingredient.price == test_data["price"]
    
    @pytest.mark.parametrize("price", [100.0, 0.0, 50.5, 999.99])
    def test_get_price_returns_correct_value(self, price):
        """Тест метода get_price с параметризацией"""
        
        ingredient = Ingredient("SAUCE", "test", price)
        
       
        assert ingredient.get_price() == price
    
    @pytest.mark.parametrize("test_data", [
        TEST_INGREDIENTS[0],  # hot sauce
        TEST_INGREDIENTS[1],  # sour cream
        TEST_INGREDIENTS[4],  # cutlet
        TEST_INGREDIENTS[5],  # dinosaur
    ])
    def test_get_name_returns_correct_value(self, test_data):
        """Тест метода get_name с параметризацией"""
       
        ingredient = Ingredient(test_data["type"], test_data["name"], 100)
        
       
        assert ingredient.get_name() == test_data["name"]
    
    @pytest.mark.parametrize("ingredient_type", ["SAUCE", "FILLING"])
    def test_get_type_returns_correct_value(self, ingredient_type):
        """Тест метода get_type с параметризацией"""
    
        ingredient = Ingredient(ingredient_type, "test", 100)
        
       
        assert ingredient.get_type() == ingredient_type
