import pytest
from praktikum.ingredient_types import *
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_price.return_value = 200.0
    mock_bun.get_name.return_value = 'White bun'
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = 300.0
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = 'Chili sauce'
    return mock_sauce


@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = 200.0
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = 'Dinosaur'
    return mock_filling
