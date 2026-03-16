import pytest
from praktikum.ingredient import Ingredient

class TestIngredient:

    def test_ingredient_initialization(self):
        ingredient = Ingredient("SAUCE", "hot sauce", 100.0)
        
        assert ingredient.type == "SAUCE"
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100.0

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient("FILLING", "cutlet", 150.0)
        assert ingredient.get_price() == 150.0

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient("SAUCE", "sour cream", 50.0)
        assert ingredient.get_name() == "sour cream"

    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient("FILLING", "sausage", 200.0)
        assert ingredient.get_type() == "FILLING"