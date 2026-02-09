import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize('ingredient_type, name, price', [
    (INGREDIENT_TYPE_SAUCE, 'hot sauce', 100),
    (INGREDIENT_TYPE_FILLING, 'cutlet', 200),
])
def test_ingredient_getters(ingredient_type, name, price):
    ing = Ingredient(ingredient_type, name, price)

    assert ing.get_type() == ingredient_type
    assert ing.get_name() == name
    assert ing.get_price() == price
