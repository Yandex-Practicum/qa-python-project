import pytest
from utils import generate_random_string, generate_random_float
from praktikum import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize('type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
    def test_ingredient(self, type):
        name = generate_random_string(10)
        price = generate_random_float()
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price
