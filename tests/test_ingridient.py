import pytest
from src.ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 100),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        """Тест создания ингредиента с разными параметрами"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_get_type(self):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_ingredient_get_name(self):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
        assert ingredient.get_name() == "cutlet"

    def test_ingredient_get_price(self):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 150.75)
        assert ingredient.get_price() == 150.75