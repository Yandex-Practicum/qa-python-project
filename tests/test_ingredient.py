import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    def test_ingredient_initialization(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
        assert ingredient.get_name() == "hot sauce"
        assert ingredient.get_price() == 100

    @pytest.mark.parametrize("ingredient_type", [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "some ingredient", 150)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["hot sauce", "cutlet", "chili sauce"])
    def test_ingredient_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [100, 200, 300])
    def test_ingredient_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", price)
        assert ingredient.get_price() == price
