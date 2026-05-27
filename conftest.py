import pytest
import data as D
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(D.BURGER_BUN_NAME, D.BURGER_BUN_PRICE)
    return bun

@pytest.fixture
def filling():
    ingredient = Ingredient(
        D.INGREDIENT_TYPE_FILLING,
        D.INGREDIENT_FILLING_NAME,
        D.INGREDIENT_FILLING_1_PRICE
    )
    return ingredient

@pytest.fixture
def sauce():
    ingredient = Ingredient(
        D.INGREDIENT_TYPE_SAUCE,
        D.INGREDIENT_SAUCE_NAME,
        D.INGREDIENT_SAUCE_PRICE
    )
    return ingredient

@pytest.fixture
def burger():
    return Burger()

