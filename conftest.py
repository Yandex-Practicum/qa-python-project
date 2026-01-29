import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'red bun'
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = 'SAUCE'
    mock_sauce.name = 'hot sauce'
    mock_sauce.price = 100.0
    mock_sauce.return_value.get_type = 'SAUCE'
    mock_sauce.return_value.get_name = 'hot sauce'
    mock_sauce.return_value.get_price = 100.0
    return mock_sauce


@pytest.fixture
def mock_bun_name_and_price():
    mock_bun = Mock()
    mock_bun.get_name.return_value = 'red bun'
    mock_bun.get_price.return_value = 100.0
    return mock_bun


@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = 'FILLING'
    mock_ingredient.name = 'cutlet'
    mock_ingredient.price = 100.0
    mock_ingredient.get_type.return_value = 'FILLING'
    mock_ingredient.get_name.return_value = 'cutlet'
    mock_ingredient.get_price.return_value = 100.0
    return mock_ingredient
