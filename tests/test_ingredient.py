import sys
import os
import pytest
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ingredient import Ingredient

@pytest.mark.parametrize("type", ["SAUCE", "FILLING"])
class TestIngredient:

    def test_ingredient_init(self, type):
        ingredient = Ingredient(type, "testIngredient", 12.99)
        assert ingredient.type == type
        assert ingredient.name == "testIngredient"
        assert ingredient.price == 12.99

    def test_ingredient_get_name(self, type):
        ingredient = Ingredient(type, "testIngredient", 12.99)
        assert ingredient.get_name() == "testIngredient"

    def test_ingredient_get_price(self, type):
        ingredient = Ingredient(type, "testIngredient", 12.99)
        assert ingredient.get_price() == 12.99

    def test_ingredient_get_type(self, type):
        ingredient = Ingredient(type, "testIngredient", 12.99)
        assert ingredient.get_type() == type