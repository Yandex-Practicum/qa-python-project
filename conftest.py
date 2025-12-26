import pytest
from unittest.mock import Mock


@pytest.fixture()
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = 'my tasty bun'
    mock.get_price.return_value = 50
    return mock

@pytest.fixture()
def ingredients_mock():
    mock_1 = Mock()
    mock_1.get_type.return_value = 'SAUCE'
    mock_1.get_name.return_value = 'spicy sauce'
    mock_1.get_price.return_value = 100
    mock_2 = Mock()
    mock_2.get_type.return_value = 'FILLING'
    mock_2.get_name.return_value = 'meat filling'
    mock_2.get_price.return_value = 200
    return [mock_1, mock_2]
