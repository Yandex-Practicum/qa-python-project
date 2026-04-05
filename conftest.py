import pytest
from selenium import webdriver
from unittest.mock import MagicMock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

from test_data import (
    BUN_PRICE, BUN_NAME,
    SAUCE_PRICE, SAUCE_NAME,
    FILLING_PRICE, FILLING_NAME
)


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def mock_bun():
    bun = MagicMock(spec=Bun)
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = SAUCE_NAME
    ingredient.get_price.return_value = SAUCE_PRICE
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture
def mock_filling():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = FILLING_NAME
    ingredient.get_price.return_value = FILLING_PRICE
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


@pytest.fixture
def burger_with_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger