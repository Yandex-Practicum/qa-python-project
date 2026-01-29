from unittest.mock import Mock
import pytest
from bun import Bun
from burger import Burger
from database import Database
from ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun("black bun", 100)
    return bun

@pytest.fixture
def ingredient():
    ingredient = Ingredient('SAUCE', 'hot sauce', 100)
    return ingredient

@pytest.fixture
def database():
    database = Database()
    return database

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_price.return_value = 200
    mock_ingredient_1.get_type.return_value = 'SAUCE'
    mock_ingredient_1.get_name.return_value = 'hot sauce'
    return mock_ingredient_1

@pytest.fixture
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_price.return_value = 300
    mock_ingredient_2.get_type.return_value = 'FILLING'
    mock_ingredient_2.get_name.return_value = 'cutlet'
    return mock_ingredient_2

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 100
    mock_bun.get_name.return_value = 'black bun'
    return mock_bun
