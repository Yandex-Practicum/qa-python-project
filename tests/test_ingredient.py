import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_FILLING, "sausage", 300)
    ])
    def test_ingredient_get_name(self, ingredient_type, name, price):
        """Проверяем получение названия ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300.50)
    ])
    def test_ingredient_get_price(self, ingredient_type, name, price):
        """Проверяем получение цены ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
    
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        ("CUSTOM_TYPE", "custom", 500)
    ])
    def test_ingredient_get_type(self, ingredient_type, name, price):
        """Проверяем получение типа ингредиента."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type