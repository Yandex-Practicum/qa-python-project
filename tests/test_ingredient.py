import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, name, price",[
        (INGREDIENT_TYPE_SAUCE, "Соус фирменный Space Sauce", 80.0),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337.0)])
    def test_ingredient_initialization_and_getters(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
