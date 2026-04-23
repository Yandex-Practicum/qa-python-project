import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientTypes:
    
    def test_sauce_type_constant(self):
        """Тест: константа SAUCE определена корректно"""
        assert INGREDIENT_TYPE_SAUCE == "SAUCE"
        assert isinstance(INGREDIENT_TYPE_SAUCE, str)
    
    def test_filling_type_constant(self):
        """Тест: константа FILLING определена корректно"""
        assert INGREDIENT_TYPE_FILLING == "FILLING"
        assert isinstance(INGREDIENT_TYPE_FILLING, str)
    
    def test_types_are_different(self):
        """Тест: типы разные"""
        assert INGREDIENT_TYPE_SAUCE != INGREDIENT_TYPE_FILLING