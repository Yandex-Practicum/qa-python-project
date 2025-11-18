import pytest
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from tests.data import TestData


class TestBurgerAddIngredient:
    """Тесты для метода add_ingredient класса Burger"""
    
    def test_add_ingredient_success(self, sample_burger, mock_sauce):
        """Тест успешного добавления ингредиента"""
        sample_burger.add_ingredient(mock_sauce)
        assert len(sample_burger.ingredients) == 1
        assert sample_burger.ingredients[0] == mock_sauce

    def test_add_ingredient_multiple(self, sample_burger, mock_sauce, mock_filling):
        """Тест добавления нескольких ингредиентов"""
        ingredient3_mock = Mock(spec=Ingredient)
        
        sample_burger.add_ingredient(mock_sauce)
        sample_burger.add_ingredient(mock_filling)
        sample_burger.add_ingredient(ingredient3_mock)
        
        assert len(sample_burger.ingredients) == 3