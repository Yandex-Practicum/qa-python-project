import pytest
from praktikum.ingredient import Ingredient
from data.data import INGREDIENT_TYPES_DATA, INGREDIENT_NAMES_DATA, INGREDIENT_PRICES_DATA

class TestIngredient:
    @pytest.mark.parametrize("ing_type", INGREDIENT_TYPES_DATA)
    def test_get_type_returns_correct_type(self, ing_type):
        ingredient = Ingredient(ing_type, "Начинка", 100)
        assert ingredient.get_type() == ing_type

    @pytest.mark.parametrize("name", INGREDIENT_NAMES_DATA)
    def test_get_name_returns_correct_name(self, name):
        ingredient = Ingredient("SAUCE", name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", INGREDIENT_PRICES_DATA)
    def test_get_price_returns_correct_price(self, price):
        ingredient = Ingredient("SAUCE", "Соус", price)
        assert ingredient.get_price() == price