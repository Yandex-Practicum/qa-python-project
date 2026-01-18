import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient

class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "salsa", 50),
            (INGREDIENT_TYPE_SAUCE, "romesco", 60),
            (INGREDIENT_TYPE_FILLING, "chicken", 50),
            (INGREDIENT_TYPE_FILLING, "tomatoes", 70),
        ]
    )
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "salsa", 50),
            (INGREDIENT_TYPE_SAUCE, "romesco", 60),
            (INGREDIENT_TYPE_FILLING, "chicken", 50),
            (INGREDIENT_TYPE_FILLING, "tomatoes", 70),
        ]
    )
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "salsa", 50),
            (INGREDIENT_TYPE_SAUCE, "romesco", 60),
            (INGREDIENT_TYPE_FILLING, "chicken", 50),
            (INGREDIENT_TYPE_FILLING, "tomatoes", 70),
        ]
    )
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
