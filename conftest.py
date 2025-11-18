import pytest
from unittest.mock import Mock
from data import BunData, IngredientData


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = BunData.bun_name
    mock.get_price.return_value = BunData.bun_price_int
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_name.return_value = IngredientData.ingredient_name
    mock.get_price.return_value = IngredientData.ingredient_price_int
    mock.get_type.return_value = IngredientData.sauce_type
    return mock