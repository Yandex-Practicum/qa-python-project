from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from data import Data
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient


@pytest.fixture
def bun():
    bun = Bun(Data.bun_name, Data.bun_price)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = Data.bun_name
    mock_bun.price = Data.bun_price
    mock_bun.get_price.return_value = Data.bun_price
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get.return_value = Data.ingredient_data
    return mock_ingredient


@pytest.fixture(scope='function')
def database():
    return Database()


@pytest.fixture(scope='function')
def ingredient():
    return Ingredient(*Data.ingredient)


@pytest.fixture(scope='function')
def ingredient_1():
    return Ingredient(*Data.ingredient_1)

