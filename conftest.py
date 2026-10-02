import pytest

from data import Data
from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE, 
    INGREDIENT_TYPE_FILLING
    )


@pytest.fixture
def database():
    return Database()


@pytest.fixture
def bun():
    return Bun(Data.BUN_1, Data.BUN_1_PRICE)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def sauce_1():
    return Ingredient(
        INGREDIENT_TYPE_SAUCE,
        Data.SAUCE_1,
        Data.SAUCE_1_PRICE
    )


@pytest.fixture
def sauce_2():
    return Ingredient(
        INGREDIENT_TYPE_SAUCE,
        Data.SAUCE_2,
        Data.SAUCE_2_PRICE
    )


@pytest.fixture
def sauce_3():
    return Ingredient(
        INGREDIENT_TYPE_SAUCE,
        Data.SAUCE_3,
        Data.SAUCE_3_PRICE
    )


@pytest.fixture
def filling_1():
    return Ingredient(
        INGREDIENT_TYPE_FILLING,
        Data.FILLING_1,
        Data.FILLING_1_PRICE
    )


@pytest.fixture
def filling_3():
    return Ingredient(
        INGREDIENT_TYPE_FILLING,
        Data.FILLING_3,
        Data.FILLING_3_PRICE
    )
