from unittest.mock import Mock
import pytest


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'sweet_bun'
    mock_bun.get_price.return_value = 88
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = 'hot sauce'
    mock_ingredient.get_type.return_value = 'filling'
    mock_ingredient.get_price.return_value = 100
    return mock_ingredient
@pytest.fixture
def mock_get_price_burger():
    mock_get_price = Mock()
    mock_get_price.return_value = 100
    return mock_get_price

@pytest.fixture
def mock_get_name_bun():
    mock_get_name = Mock()
    mock_get_name.return_value = 'hot sauce'
    return mock_get_name


@pytest.fixture
def mock_get_price_bun():
    mock_get_price = Mock()
    mock_get_price.return_value = 100
    return mock_get_price


