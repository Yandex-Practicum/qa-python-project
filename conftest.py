import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "white bun"
    mock.get_price.return_value = 200
    return mock

@pytest.fixture
def ingredient_factory():
    def _create(name="default", price=100, type="SAUCE"):
        mock = Mock()
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        mock.get_type.return_value = type
        return mock
    return _create

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()
