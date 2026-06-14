from ingredient import Ingredient
import pytest
from ingredient_types import INGREDIENT_TYPE_SAUCE,INGREDIENT_TYPE_FILLING

class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price",
    [(INGREDIENT_TYPE_SAUCE, "Лунный Тар-Тар", 50),(INGREDIENT_TYPE_FILLING, "Метеоритная котлета", 150)])
    def test_ingredient_getters_success(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price
        assert ingredient.get_name() == name
        assert ingredient.get_type() == ingredient_type
        