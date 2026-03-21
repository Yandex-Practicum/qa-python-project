import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize("ing_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_get_type_returns_correct_value(self, ing_type):
        ingredient = Ingredient(ing_type, "sour cream", 100)
        assert ingredient.get_type() == ing_type

    @pytest.mark.parametrize("name", ["sour cream", "cutlet"])
    def test_get_name_returns_correct_value(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [100, 200])
    def test_get_price_returns_correct_value(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", price)
        assert ingredient.get_price() == price

    def test_initialization_sets_type_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "chicken", 150)
        assert ingredient.type == INGREDIENT_TYPE_FILLING

    def test_initialization_sets_name_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "chicken", 150)
        assert ingredient.name == "chicken"

    def test_initialization_sets_price_attribute(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "chicken", 150)
        assert ingredient.price == 150