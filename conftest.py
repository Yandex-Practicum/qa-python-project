import pytest

from praktikum.database import Database
from unittest.mock import Mock


@pytest.fixture
def db():
    return Database()


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'Краторная булочка'
    mock_bun.get_price.return_value = 1255
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_for_ingredient = Mock()
    mock_for_ingredient.get_name.return_value = 'Соус Spicy'
    mock_for_ingredient.get_price.return_value = 90
    mock_for_ingredient.get_type.return_value = 'SAUCE'
    return mock_for_ingredient
