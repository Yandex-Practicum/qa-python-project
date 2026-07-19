import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:


    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_name() == "hot sauce"

    def test_get_name_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_name() == "cutlet"


    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_price() == 100

    def test_get_price_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_price() == 150


    def test_get_type_sauce(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_get_type_filling(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 150)
        assert ingredient.get_type() == INGREDIENT_TYPE_FILLING


    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        (INGREDIENT_TYPE_FILLING, "cutlet", 150),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 250),
    ])
    def test_ingredient_creation(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price


        