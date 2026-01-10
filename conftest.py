import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    mock_ingredient_1 = Mock()
    mock_ingredient_1.name = Data.INGREDIENT_1_NAME
    mock_ingredient_1.price = Data.INGREDIENT_1_PRICE
    mock_ingredient_1.type = Data.INGREDIENT_1_TYPE
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = Data.INGREDIENT_2_NAME
    mock_ingredient_2.price = Data.INGREDIENT_2_PRICE
    mock_ingredient_2.type = Data.INGREDIENT_2_TYPE
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    return burger


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.BUN_NAME
    mock_bun.price = Data.BUN_PRICE
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.name = Data.INGREDIENT_1_NAME
    mock_ingredient_1.price = Data.INGREDIENT_1_PRICE
    mock_ingredient_1.type = Data.INGREDIENT_1_TYPE
    return mock_ingredient_1


@pytest.fixture(scope='function')
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = Data.INGREDIENT_2_NAME
    mock_ingredient_2.price = Data.INGREDIENT_2_PRICE
    mock_ingredient_2.type = Data.INGREDIENT_2_TYPE
    return mock_ingredient_2
