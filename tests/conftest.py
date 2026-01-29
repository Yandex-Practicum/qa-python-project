import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "fluorescent bun"
    mock_bun.get_price.return_value = 988
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = 90
    mock_ingredient.get_name.return_value = "sauce spicy-x"
    mock_ingredient.get_type.return_value = "sauce"
    return mock_ingredient





