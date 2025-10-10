import pytest
from unittest.mock import Mock

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_price.return_value = 200
    mock.get_name.return_value = 'Булка'
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_price.return_value = 200
    mock.get_name.return_value = 'Ингредиент'
    mock.get_type.return_value = 'SAUCE'
    return mock
