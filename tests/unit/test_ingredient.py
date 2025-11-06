import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.mark.parametrize("type_, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150.0),
])
def test_ingredient_creation_and_getters(type_, name, price):
    ing = Ingredient(type_, name, price)
    assert ing.get_name() == name
    assert ing.get_type() == type_
    assert ing.get_price() == price

def test_ingredient_type_constants_values():
    assert INGREDIENT_TYPE_SAUCE == "SAUCE"
    assert INGREDIENT_TYPE_FILLING == "FILLING"