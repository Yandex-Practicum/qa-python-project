import sys
from unittest.mock import MagicMock, Mock

sys.modules['praktikum'] = MagicMock()
sys.modules['praktikum.bun'] = MagicMock()
sys.modules['praktikum.ingredient'] = MagicMock()
sys.modules['praktikum.bun'].Bun = Mock()
sys.modules['praktikum.ingredient'].Ingredient = Mock()

from Diplom_1.burger import Burger
from .mocks import create_mock_bun, create_mock_ingredient

import pytest

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    return create_mock_bun()

@pytest.fixture
def mock_sauce():
    return create_mock_ingredient(ingredient_type="sauce", name="hot sauce", price=50)

@pytest.fixture
def mock_filling():
    return create_mock_ingredient(ingredient_type="filling", name="cheese", price=70)
