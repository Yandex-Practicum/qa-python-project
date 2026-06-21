import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from unittest.mock import Mock
import data

@pytest.fixture()
def bun():
    bun = Bun(data.BUN_NAME, data.BUN_PRICE)
    return bun

@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    mock_bun.configure_mock(name=data.BUN_NAME)
    mock_bun.configure_mock(price=data.BUN_PRICE)
    return mock_bun

@pytest.fixture()
def burger():
    burger = Burger()
    return burger

@pytest.fixture()
def ingredient():
    ingredient = Ingredient(data.INGR_TYPE, data.INGR_NAME, data.INGR_PRICE)
    return ingredient

@pytest.fixture()
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.configure_mock(type=data.INGR_TYPE)
    mock_ingredient.configure_mock(name=data.INGR_NAME)
    mock_ingredient.configure_mock(price=data.INGR_PRICE)
    return mock_ingredient

@pytest.fixture()
def database():
    database = Database()
    return database