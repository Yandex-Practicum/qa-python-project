import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

BUN_PRICE = 50
BUN_NAME_1 = "Test Bun 1"
BUN_NAME_2 = "Test Bun 2"
SAUCE_NAME = "Test Sauce"
FILLING_NAME = "Test Filling"
SAUCE_PRICE = 20
FILLING_PRICE = 40


@pytest.fixture
def mock_bun():
    return Bun(BUN_NAME_1, BUN_PRICE)


@pytest.fixture
def mock_bun_2():
    return Bun(BUN_NAME_2, BUN_PRICE)


@pytest.fixture
def mock_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, SAUCE_NAME, SAUCE_PRICE)


@pytest.fixture
def mock_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)


@pytest.fixture
def burger():
    return Burger()
