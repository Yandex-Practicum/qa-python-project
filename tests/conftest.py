import pytest
import sys
from pathlib import Path
from unittest.mock import MagicMock
from praktikum.database import Database
from praktikum.burger import Burger

sys.path.append(str(Path(__file__).parent.parent))

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "Краторная булка"
    bun.get_price.return_value = 100.0
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_name.return_value = "Сыр"
    ingredient.get_price.return_value = 50.0
    ingredient.get_type.return_value = "FILLING"
    return ingredient


