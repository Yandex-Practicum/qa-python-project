import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    def setup_method(self):
        self.ingredient = Ingredient("FILLING", "Сыр", 50.0)
    
    def test_get_price(self):
        """Тестируем получение цены ингредиента"""
        assert self.ingredient.get_price() == 50.0
    
    def test_get_name(self):
        """Тестируем получение названия ингредиента"""
        assert self.ingredient.get_name() == "Сыр"
    
    def test_get_type(self):
        """Тестируем получение типа ингредиента"""
        assert self.ingredient.get_type() == "FILLING"
    
    @pytest.mark.parametrize("ingredient_type,name,price", [
        ("FILLING", "Сыр", 50.0),
        ("SAUCE", "Соус", 30.0),
        ("FILLING", "Котлета", 100.0),
        ("SAUCE", "Горчица", 10.0)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        """Тестируем инициализацию ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price