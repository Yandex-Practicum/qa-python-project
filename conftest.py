import pytest
from praktikum.bun import Bun
from data import DataBun, DataIngredient
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def new_bun():
    """Фикстура для тестирования класса Bun"""
    bun = Bun(DataBun.BUN_NAME, DataBun.BUN_PRICE)

    return bun

@pytest.fixture
def new_ingredient():
    """Фикстура для тестирования класса Ingredient"""
    ingredient = Ingredient(
        DataIngredient.INGREDIENT_TYPE_FILLING,
        DataIngredient.INGREDIENT_NAME,
        DataIngredient.INGREDIENT_PRICE
    )

    return ingredient

@pytest.fixture
def new_burger():
    """Фикстура для тестирования класса Burger"""
    burger = Burger()

    return burger

@pytest.fixture
def new_database():
    database = Database()

    return database
