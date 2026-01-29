import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_type(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type

    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_name(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("type, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "hot sauce", 100), (INGREDIENT_TYPE_FILLING, "cutlet", 100), ], )
    def test_ingredient_get_price(self, type, name, price):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_price() == price
