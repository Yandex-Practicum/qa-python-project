from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
import pytest


@pytest.fixture(scope='function')
def bun():
    bun = Bun('CherryBun', 123)
    return bun


@pytest.fixture(scope='function')
def burger():
    burger = Burger()
    return burger


@pytest.fixture(scope='function')
def database():
    database = Database()
    return database


@pytest.fixture(scope='function')
def ingridient():
    ingridient = Ingredient('filling', 'onion', 50)
    return ingridient


@pytest.fixture(scope='function')
def mock_ingridient():
    ingridient = Mock()
    ingridient.get_type = 'Souce'
    ingridient.get_name.return_value = 'Meat'
    ingridient.get_price.return_value = 88

    return ingridient


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "CherryBun"
    bun.get_price.return_value = 123

    return bun
