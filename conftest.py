import pytest
from data import BUN_DATA, SAUCE_DATA
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture()
def bun_fixture():
    name = next(iter(BUN_DATA))
    price = BUN_DATA[name]
    bun = Bun(name, price)    
    return bun

@pytest.fixture()
def ingredient_fixture():
    type = INGREDIENT_TYPE_SAUCE
    name = next(iter(SAUCE_DATA))
    price = SAUCE_DATA[name]    
    sauce = Ingredient(type, name, price)    
    return sauce