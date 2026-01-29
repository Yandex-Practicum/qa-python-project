import pytest

from unittest.mock import Mock
from data import Data


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = Data.BUN_NAME[0]
    mock_bun.get_price.return_value = Data.BUN_PRICE[0]
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = Data.ING_NAME
    mock_ingredient.get_type.return_value = Data.ING_TYPE
    mock_ingredient.get_price.return_value = Data.BUN_PRICE
    return mock_ingredient
