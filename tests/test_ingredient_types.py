import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum import ingredient_types


class TestIngredientTypes:
  

    def test_constants_exist(self):
        assert hasattr(ingredient_types, 'INGREDIENT_TYPE_SAUCE')
        assert hasattr(ingredient_types, 'INGREDIENT_TYPE_FILLING')

    def test_constants_values(self):
        assert ingredient_types.INGREDIENT_TYPE_SAUCE == 'SAUCE'
        assert ingredient_types.INGREDIENT_TYPE_FILLING == 'FILLING'

    def test_constants_are_strings(self):
        assert isinstance(ingredient_types.INGREDIENT_TYPE_SAUCE, str)
        assert isinstance(ingredient_types.INGREDIENT_TYPE_FILLING, str)