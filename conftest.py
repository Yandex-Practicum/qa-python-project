import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.database import Database
from test_data import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from unittest.mock import Mock


@pytest.fixture
def bun():
    return Bun(BUN_NAME, BUN_PRICE)

@pytest.fixture
def ingredient_factory():
    def _create(ingredient_type, name, price):
        return Ingredient(ingredient_type, name, price)
    return _create

@pytest.fixture
def sauce_ingredient(ingredient_factory):
    return ingredient_factory(
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_NAME,
        INGREDIENT_PRICE
    )

@pytest.fixture
def filling_ingredient(ingredient_factory):
    return ingredient_factory(INGREDIENT_TYPE_FILLING, FILLING_NAME, FILLING_PRICE)

@pytest.fixture
def burger() -> Burger:
    return Burger()

@pytest.fixture
def db() -> Database:
    return Database()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = MOCK_BUN_NAME
    bun.get_price.return_value = MOCK_BUN_PRICE
    return bun

@pytest.fixture
def mock_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = SAUCE_NAME
    ingredient.get_price.return_value = SAUCE_PRICE
    return ingredient

@pytest.fixture
def mock_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = FILLING_NAME
    ingredient.get_price.return_value = FILLING_PRICE
    return ingredient

@pytest.fixture
def mock_ingredient_factory():
    def _create(ingredient_type, name, price):
        ingredient = Mock(spec=["get_type", "get_name", "get_price"])
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient
    return _create
