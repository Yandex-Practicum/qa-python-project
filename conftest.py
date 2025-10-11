import pytest
from unittest.mock import Mock

import data


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = data.DEF_BUN_NAME
    mock_bun.price = data.DEF_BUN_PRICE
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = data.DEF_INGREDIENT_TYPE
    mock_ingredient.name = data.DEF_INGREDIENT_NAME
    mock_ingredient.price = data.DEF_INGREDIENT_PRICE
    return mock_ingredient

@pytest.fixture
def mock_burger(mock_bun, mock_ingredient):
    mock_burger = Mock()
    mock_burger.bun = mock_bun
    mock_burger.ingredient = [mock_ingredient]
    return mock_burger
