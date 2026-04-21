import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    
    def test_get_name_returns_correct_ingredient_name(self):
        ingredient = Ingredient("SAUCE", "Соус Spicy-X", 90.0)
        assert ingredient.get_name() == "Соус Spicy-X"
    
    def test_get_price_returns_correct_ingredient_price(self):
        ingredient = Ingredient("SAUCE", "Соус Spicy-X", 90.0)
        assert ingredient.get_price() == 90.0
    
    @pytest.mark.parametrize("ingredient_type", [
        "SAUCE",
        "FILLING"
    ])
    def test_get_type_returns_correct_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Тестовый ингредиент", 100.0)
        assert ingredient.get_type() == ingredient_type