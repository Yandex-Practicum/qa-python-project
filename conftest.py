from unittest.mock import Mock, patch

import pytest
from data import BUN, BUN2, INGREDIENT, INGREDIENT2, BUNS_DATA, INGR_DATA
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database


@pytest.fixture(scope='session')
def test_bun():
    return Bun(**BUN)  # Create Bun object


@pytest.fixture(scope='session')
def test_bun2():
    return Bun(**BUN2)


@pytest.fixture(scope='session')
def test_burger():
    return Burger()  # Create Burger object


@pytest.fixture(scope='session')
def test_ingredient():
    return Ingredient(**INGREDIENT)  # Create Ingredient object


@pytest.fixture(scope='session')
def test_ingredient2():
    return Ingredient(**INGREDIENT2)  # Create Ingredient object


@pytest.fixture(scope='session')
def mock():
    return Mock()  # Create Mock


@pytest.fixture(scope='session')
def mock_bun(mock):
    mock.configure_mock(**BUN)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    return mock  # Create mock for bun


@pytest.fixture(scope='session')
def mock_ingredient(mock):
    mock.configure_mock(**INGREDIENT)
    mock.get_name.return_value = mock.name
    mock.get_price.return_value = mock.price
    mock.get_type.return_value = mock.type
    return mock  # Create mock for ingredient


@pytest.fixture(scope='session')
def mock_ingredients_list():
    ingredients = []
    for _type, name, price in INGR_DATA:
        mock = Mock()
        mock.configure_mock(type=_type, name=name, price=price)
        mock.get_name.return_value = mock.name
        mock.get_type.return_value = mock.type
        mock.get_price.return_value = mock.price
        ingredients.append(mock)
    return ingredients  # ingredients list mock


@pytest.fixture(scope='session')
def mock_buns_list(mock):
    buns = []
    for name, price in BUNS_DATA:
        mock = Mock()
        mock.configure_mock(name=name, price=price)
        mock.get_name.return_value = mock.name
        mock.get_price.return_value = mock.price
        buns.append(mock)
    return buns  # returns list of bun mocks


@pytest.fixture(scope='session')
@patch('praktikum.database.Ingredient')
@patch('praktikum.database.Bun')
def test_database(
        mock_bun_init, mock_ingredient_init, mock_buns_list, mock_ingredients_list
):
    mock_bun_init.side_effect = mock_buns_list
    mock_ingredient_init.side_effect = mock_ingredients_list
    return Database()  # returns test Database object with patched Ingredient and Bun
