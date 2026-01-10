import pytest
from unittest.mock import Mock

import praktikum.ingredient_types


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = 'black bun'
    mock_bun.price = 100
    return mock_bun


@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = praktikum.ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = 'hot sauce'
    mock_ingredient.price = 100
    return mock_ingredient
