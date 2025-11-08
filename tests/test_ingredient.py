import pytest

from src.ingredient import Ingredient
from src.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.mark.parametrize("itype,name,price", [
    (INGREDIENT_TYPE_SAUCE, "BBQ", 0.8),
    (INGREDIENT_TYPE_FILLING, "Beef", 3.2),
])
def test_ingredient_valid(itype, name, price):
    ing = Ingredient(ingredient_type=itype, name=name, price=price)

    assert ing.get_type() == itype
    assert ing.get_name() == name
    assert ing.get_price() == price
