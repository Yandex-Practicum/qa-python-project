
import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger
from data import TestData


@pytest.fixture(scope="function")
def create_bun():
    bun = Bun("Test Bun", 10.5)
    return bun

@pytest.fixture(scope="function")
def create_base():
    database = Database()
    return database

@pytest.fixture(scope="function")
def burger():
    burger = Burger()
    return burger

@pytest.fixture(scope="function")
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = TestData.buns[0][0]
    mock_bun.get_price.return_value = TestData.buns[0][1]
    return mock_bun

@pytest.fixture(scope="function")
def ingredients_mock():
    mock_ingredient = Mock()
    mock_ingredient.name = TestData.ingredients[0][1]
    mock_ingredient.price = TestData.ingredients[0][2]
    mock_ingredient.get_price.return_value = TestData.ingredients[0][2]
    mock_ingredient.get_name.return_value = TestData.ingredients[0][1]
    mock_ingredient.get_type.return_value = TestData.ingredients[0][0]
    return mock_ingredient

@pytest.fixture(scope="function")
def ingredients_mock_add():
    mock_ingredient_add = Mock()
    mock_ingredient_add.name = TestData.ingredients[3][1]
    mock_ingredient_add.price = TestData.ingredients[3][2]
    mock_ingredient_add.get_price.return_value = TestData.ingredients[3][2]
    mock_ingredient_add.get_name.return_value = TestData.ingredients[3][1]
    mock_ingredient_add.get_type.return_value = TestData.ingredients[3][0]
    return mock_ingredient_add