import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200.0),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100.0),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200.0),
        ],
    )
    def test_ingredient_init_and_getters(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price

    def test_ingredient_attributes(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == "hot sauce"
        assert ingredient.price == 100.0