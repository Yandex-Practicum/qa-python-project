import sys
from pathlib import Path
from unittest.mock import Mock
import pytest


sys.path.insert(0, str(Path(__file__).parent.parent))

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = 'test_bun'
    bun.get_price.return_value = 89.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = Mock()
    ingredient.get_price.return_value = 99.0
    ingredient.get_name.return_value = 'test_ingredient'
    ingredient.get_type.return_value = 'FILLING'
    return ingredient
