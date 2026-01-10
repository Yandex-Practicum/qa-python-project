from unittest.mock import Mock
import pytest
from data import Data

@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.name = Data.BUN_NAME_MOCKED
    mock.get_name.return_value = Data.BUN_NAME_MOCKED
    mock.get_price.return_value = Data.BUN_PRICE_MOCKED
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.name = Data.INGREDIENT_NAME_MOCKED
    mock.get_name.return_value = Data.INGREDIENT_NAME_MOCKED
    mock.get_price.return_value = Data.INGREDIENT_PRICE_MOCKED
    mock.get_type.return_value = Data.INGREDIENT_TYPE_MOCKED
    return mock