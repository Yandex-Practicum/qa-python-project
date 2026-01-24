import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, "cheese", 30),
                                                                  (INGREDIENT_TYPE_FILLING, "bacon", 90)])
    def test_get_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, "ketchup", 30),
                                                              (INGREDIENT_TYPE_SAUCE, "mayo", 30),
                                                              (INGREDIENT_TYPE_FILLING, "lettuce", 90)])
    def test_get_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type, name, price", [(INGREDIENT_TYPE_SAUCE, "bbq", 30),
                                                             (INGREDIENT_TYPE_FILLING, "bacon", 90),
                                                            (INGREDIENT_TYPE_FILLING, "onion", 15)])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type
