import pytest
from unittest.mock import Mock

@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = "Test Bun"
    mock.get_price.return_value = 2.5
    return mock


@pytest.fixture
def ingredient_mock():
    def _create(type_, name, price):
        mock = Mock()
        mock.get_type.return_value = type_
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock
    return _create


@pytest.fixture
def ingredient_mock_filling():
    mock = Mock()
    mock.get_type.return_value = "FILLING"
    mock.get_name.return_value = "Meat"
    mock.get_price.return_value = 3.0
    return mock


@pytest.fixture
def ingredient_mock_sauce():
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "Ketchup"
    mock.get_price.return_value = 1.5
    return mock