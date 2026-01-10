import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
sys.path.insert(0, str(Path(__file__).parent.parent))

from helpers import create_mock_ingredient, create_mock_bun
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def white_bun():
    return create_mock_bun("White Bun", 100.0)

@pytest.fixture
def black_bun():
    return create_mock_bun("Black Bun", 150.0)

@pytest.fixture
def sauce_ingredient():
    return create_mock_ingredient("spicy sauce", INGREDIENT_TYPE_SAUCE, 90.0)

@pytest.fixture
def filling_ingredient():
    return create_mock_ingredient("Cutlet", INGREDIENT_TYPE_FILLING, 100.0)

@pytest.fixture(params=[1, 3, 5, 10])
def ingredient_count(request):
    return request.param
