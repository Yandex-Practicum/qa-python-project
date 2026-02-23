import os
import sys

import pytest
from unittest.mock import Mock


# Ensure the project root (where the `praktikum/` package lives) is importable.
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = 'test bun'
    bun.get_price.return_value = 50.0
    return bun


@pytest.fixture
def ingredient_mock():
    ingr = Mock()
    ingr.get_type.return_value = 'SAUCE'
    ingr.get_name.return_value = 'hot sauce'
    ingr.get_price.return_value = 10.0
    return ingr
