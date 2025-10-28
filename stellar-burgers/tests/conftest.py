import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import (
    TEST_BUN_NAME_RU as TEST_BUN_NAME,
    TEST_BUN_PRICE,
    TEST_SAUCE_NAME_RU as TEST_SAUCE_NAME,
    TEST_SAUCE_PRICE,
    FILLING_NAME as TEST_FILLING_NAME,
    FILLING_PRICE as TEST_FILLING_PRICE
)


@pytest.fixture
def sample_bun():
    """Фикстура для создания тестовой булочки."""
    return Bun(TEST_BUN_NAME, TEST_BUN_PRICE)

@pytest.fixture
def sample_sauce():
    """Фикстура для создания тестового соуса."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, TEST_SAUCE_NAME, TEST_SAUCE_PRICE)

@pytest.fixture
def sample_filling():
    """Фикстура для создания тестовой начинки."""
    return Ingredient(INGREDIENT_TYPE_FILLING, TEST_FILLING_NAME, TEST_FILLING_PRICE)


@pytest.fixture
def empty_burger():
    """Фикстура для создания пустого бургера."""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def prepared_burger(empty_burger, sample_bun, sample_sauce, sample_filling):
    """Фикстура для создания собранного бургера."""
    empty_burger.set_buns(sample_bun)
    empty_burger.add_ingredient(sample_sauce)
    empty_burger.add_ingredient(sample_filling)
    return empty_burger