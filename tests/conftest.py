import os
import sys
from unittest.mock import Mock

import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_price.return_value = 2.5
    bun.get_name.return_value = "Sesame Bun"
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    ing = Mock()
    ing.get_price.return_value = 1.0
    ing.get_name.return_value = "BBQ"
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ing


@pytest.fixture
def mock_ingredient_filling():
    ing = Mock()
    ing.get_price.return_value = 3.0
    ing.get_name.return_value = "Beef"
    ing.get_type.return_value = "FILLING"
    return ing
