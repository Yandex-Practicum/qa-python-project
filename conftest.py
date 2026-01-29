import pytest
from unittest.mock import Mock
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "bun"
    mock.get_price.return_value = 200
    return mock


@pytest.fixture()
def mock_sauce():
    mock = Mock()
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture()
def mock_filling():
    mock = Mock()
    mock.get_name.return_value = "cutlet"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture()
def mock_database():
    db = Database()
    return db
