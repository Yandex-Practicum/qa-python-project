import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "sausage", 300),
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 50)

        assert ingredient.get_name() == "sausage"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 50)

        assert ingredient.get_price() == 50

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 50)

        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE