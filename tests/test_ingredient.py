from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
import pytest

class TestIngredient:
    
    def test_get_price_with_exist_ingredient_price_returns_ingredient_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

        assert ingredient.get_price() == 200

    def test_get_name_with_exist_ingredient_returns_ingredient_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)

        assert ingredient.get_name() == "dinosaur"

    @pytest.mark.parametrize('ingredient_type, name, price', [[INGREDIENT_TYPE_SAUCE, "hot sauce", 100],
                                                              [INGREDIENT_TYPE_FILLING, "dinosaur", 200]])
    def test_get_type_with_exist_ingredient_type_returns_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type