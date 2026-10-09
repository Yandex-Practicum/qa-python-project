import pytest
import sys
import os
from unittest.mock import MagicMock

project_root = os.path.dirname(os.path.abspath(__file__))
praktikum_path = os.path.join(project_root, '..', 'praktikum')
if praktikum_path not in sys.path:
    sys.path.insert(0, praktikum_path)

fake_bun = MagicMock()
fake_bun.get_name.return_value = "Mock Bun"
fake_bun.get_price.return_value = 50.0

fake_ingredient = MagicMock()
fake_ingredient.get_name.return_value = "Mock Ingredient"
fake_ingredient.get_price.return_value = 30.0
fake_ingredient.get_type.return_value = "filling"

sys.modules['praktikum'] = MagicMock()
sys.modules['praktikum.bun'] = MagicMock()
sys.modules['praktikum.bun'].Bun = fake_bun
sys.modules['praktikum.ingredient'] = MagicMock()
sys.modules['praktikum.ingredient'].Ingredient = fake_ingredient

@pytest.fixture
def burger():

    from burger import Burger
    return Burger()

@pytest.fixture
def mock_bun():
    return fake_bun

@pytest.fixture
def mock_ingredient():
    return fake_ingredient