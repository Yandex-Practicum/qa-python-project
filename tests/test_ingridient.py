import pytest
from practikum.ingredient import Ingredient
from practikum import ingredient_types


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "Tomato Sauce", 1.5),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "Cheese", 2.0),
    ])
    def test_initialization_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "Tomato Sauce", 1.5),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "Cheese", 2.0),
    ])
    def test_initialization_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "Tomato Sauce", 1.5),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "Cheese", 2.0),
    ])
    def test_initialization_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    def test_get_name(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_SAUCE, "Tomato Sauce", 1.5)
        assert ingredient.get_name() == "Tomato Sauce"

    def test_get_price(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "Cheese", 2.0)
        assert ingredient.get_price() == 2.0

    def test_get_type(self):
        ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING, "Chicken", 3.0)
        assert ingredient.get_type() == ingredient_types.INGREDIENT_TYPE_FILLING
