import pytest
from constsnts import Constants
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun_fix():
    bun = Bun(name=Constants.BUN, price=Constants.BUT_PRICE)
    return bun


@pytest.fixture
def ingredient_fix():
    ingredient = Ingredient(ingredient_type=Constants.INGREDIENT_TYPE, name=Constants.INGREDIENT_NAME,
                            price=Constants.INGREDIENT_PRICE)
    return ingredient


@pytest.fixture
def ingredient_filling_fix():
    ingredient = Ingredient(ingredient_type=Constants.INGREDIENT_TYPE_FILLING, name=Constants.INGREDIENT_FILLING_NAME,
                            price=Constants.INGREDIENT_FILLING_PRICE)
    return ingredient
