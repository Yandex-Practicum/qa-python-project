import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "yellow bun"
    mock_bun.get_price.return_value = 400
    return mock_bun

@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_name.return_value = "teriyaki"
    mock_sauce.get_price.return_value = 400
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock_sauce

@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_name.return_value = "snake"
    mock_filling.get_price.return_value = 400
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock_filling
