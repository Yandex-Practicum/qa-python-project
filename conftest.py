import pytest
import ingredient_types
from unittest.mock import Mock


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = ingredient_types.BUN_NAME
    mock_bun.get_price.return_value = ingredient_types.BUN_PRICE
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    mock_ingredient.get_name.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_ingredient.get_price.return_value = ingredient_types.INGREDIENT_PRICE
    return mock_ingredient
