import pytest
from unittest.mock import Mock
from data import Data


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = Data.BUN_PRICE
    mock_bun.get_name.return_value = Data.BUN_NAME

    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_price.return_value = Data.INGREDIENT_PRICE
    mock_ingredient.get_name.return_value = Data.INGREDIENT_NAME
    mock_ingredient.get_type.return_value = Data.INGREDIENTS_TYPE

    return mock_ingredient


@pytest.fixture(scope='function')
def mock_ingredient_second_from_move_test():
    mock_second_ingredient = Mock()
    mock_second_ingredient.get_price.return_value = Data.SECOND_INGREDIENT_PRICE
    mock_second_ingredient.get_name.return_value = Data.SECOND_INGREDIENT_NAME
    mock_second_ingredient.get_type.return_value = Data.SECOND_INGREDIENTS_TYPE

    return mock_second_ingredient
