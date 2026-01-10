"""
Тесты для класса Ingredient
"""
import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.test_data import (
    INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_NAME_2, INGREDIENT_PRICE_2,
    INGREDIENT_TYPE_SAUCE as SAUCE_TYPE, INGREDIENT_TYPE_FILLING as FILLING_TYPE
)


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_ingredient_creation(self):
        """Тест создания объекта ингредиента"""
        ingredient = Ingredient(SAUCE_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
        
        assert ingredient.type == SAUCE_TYPE
        assert ingredient.name == INGREDIENT_NAME
        assert ingredient.price == INGREDIENT_PRICE

    def test_get_price(self):
        """Тест метода get_price"""
        ingredient = Ingredient(SAUCE_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
        
        result = ingredient.get_price()
        
        assert result == INGREDIENT_PRICE

    def test_get_name(self):
        """Тест метода get_name"""
        ingredient = Ingredient(SAUCE_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
        
        result = ingredient.get_name()
        
        assert result == INGREDIENT_NAME

    def test_get_type(self):
        """Тест метода get_type"""
        ingredient = Ingredient(SAUCE_TYPE, INGREDIENT_NAME, INGREDIENT_PRICE)
        
        result = ingredient.get_type()
        
        assert result == SAUCE_TYPE

    def test_ingredient_filling_type(self):
        """Тест ингредиента типа начинка"""
        ingredient = Ingredient(FILLING_TYPE, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
        
        assert ingredient.get_type() == FILLING_TYPE
        assert ingredient.get_name() == INGREDIENT_NAME_2
        assert ingredient.get_price() == INGREDIENT_PRICE_2

    def test_ingredient_with_fixture(self, ingredient):
        """Тест ингредиента с использованием фикстуры"""
        assert ingredient.get_type() == SAUCE_TYPE
        assert ingredient.get_name() == INGREDIENT_NAME
        assert ingredient.get_price() == INGREDIENT_PRICE

    def test_ingredient_filling_with_fixture(self, ingredient_filling):
        """Тест ингредиента-начинки с использованием фикстуры"""
        assert ingredient_filling.get_type() == FILLING_TYPE
        assert ingredient_filling.get_name() == INGREDIENT_NAME_2
        assert ingredient_filling.get_price() == INGREDIENT_PRICE_2 