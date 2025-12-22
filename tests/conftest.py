import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from data import BurgerIngredients
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def create_bun():
    bun = Bun(BurgerIngredients.TEST_BUN_NAME, BurgerIngredients.TEST_BUN_PRICE)
    return bun

@pytest.fixture
def create_ingredient():
    ingredient = Ingredient(BurgerIngredients.TEST_INGREDIENT_TYPE, BurgerIngredients.TEST_INGREDIENT_NAME, BurgerIngredients.TEST_INGREDIENT_PRICE)
    return ingredient

@pytest.fixture
def create_database():
    database = Database()
    return database

@pytest.fixture
def create_burger():
    test_burger = Burger()
    return test_burger
