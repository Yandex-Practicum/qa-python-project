import pytest
from data import *
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


@pytest.mark.parametrize('ingredient_type', [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
class TestIngredient:
    def test_bun_init(self, ingredient_type):
        price = get_random_value(PRICES)
        name = get_random_value(SAUCES_NAMES) if ingredient_type == 'SAUCE' else get_random_value(FILLINGS_NAMES)
        ingredient = Ingredient(ingredient_type, name, price)

        assert (ingredient.get_price() == price
                and ingredient.get_name() == name
                and ingredient.get_type() == ingredient_type)
