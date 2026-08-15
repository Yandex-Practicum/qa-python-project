import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 50.0),
        (INGREDIENT_TYPE_FILLING, "cutlet", 120.0),
    ])
    def test_ingredient_creation(self, ing_type, name, price):
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.type == ing_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 75.5)
        assert ingredient.get_price() == 75.5

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)
        assert ingredient.get_name() == "dinosaur"

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE
