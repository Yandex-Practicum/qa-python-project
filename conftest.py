import pytest

from unittest.mock import Mock
from praktikum.burger import Burger
from data import Data


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    mock_ingredient_1 = Mock()
    mock_ingredient_1.name = Data.IngredientName1
    mock_ingredient_1.price = Data.IngredientPrice1
    mock_ingredient_1.type = Data.IngredientType1
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = Data.IngredientName2
    mock_ingredient_2.price = Data.IngredientPrice2
    mock_ingredient_2.type = Data.IngredientType2
    burger.add_ingredient(mock_ingredient_1)
    burger.add_ingredient(mock_ingredient_2)
    return burger

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.BunName
    mock_bun.price = Data.BumPrice
    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.name = Data.IngredientName1
    mock_ingredient_1.price = Data.IngredientPrice1
    mock_ingredient_1.type = Data.IngredientType1
    return mock_ingredient_1

@pytest.fixture(scope='function')
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.name = Data.IngredientName2
    mock_ingredient_2.price = Data.IngredientPrice2
    mock_ingredient_2.type = Data.IngredientType2
    return mock_ingredient_2