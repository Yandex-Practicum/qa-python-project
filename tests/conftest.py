import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    bun = Bun(name="Булочка", price=10.5)
    return bun
@pytest.fixture
def ingredient_filling():
    filling_ingredient = Ingredient(INGREDIENT_TYPE_FILLING, 'Биокотлета из марсианской Магнолии', 90.00)
    return filling_ingredient
@pytest.fixture
def ingredient_sauce():
    sauce_ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус фирменный Space Sauce', 4.00)
    return sauce_ingredient

