# conftest.py

import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "black bun"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def empty_burger():
    from praktikum.burger import Burger
    return Burger()