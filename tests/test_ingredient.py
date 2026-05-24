import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_ingredient_creation_returns_correct_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_ingredient_creation_returns_correct_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_ingredient_creation_returns_correct_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
    
    def test_ingredient_get_price_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 150)
        assert ingredient.get_price() == 150
    
    def test_ingredient_get_name_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert ingredient.get_name() == "cutlet"
    
    def test_ingredient_get_type_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE