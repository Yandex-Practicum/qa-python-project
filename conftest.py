import pytest
from unittest.mock import MagicMock

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


from bun import Bun

from burger import Burger
from database import Database
from helpers.data import BUNS_INFO, INGREDIENTS_INFO
from ingredient import Ingredient


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_create_buns():
    bun_mock = MagicMock(spec=Bun)
    bun_mock.get_name.return_value = BUNS_INFO[0]["bun_name"]
    bun_mock.get_price.return_value = BUNS_INFO[0]["bun_price"]
    return bun_mock

@pytest.fixture
def mock_create_ingredient():
    ingredient_mock = MagicMock(spec=Ingredient)

    ingredient_mock.get_name.return_value = INGREDIENTS_INFO[0]["ingredient_name"]
    ingredient_mock.get_type.return_value = INGREDIENTS_INFO[0]["ingredient_type"]
    ingredient_mock.get_price.return_value = INGREDIENTS_INFO[0]["ingredient_price"]

    return ingredient_mock

@pytest.fixture
def mock_create_additional_ingredient():
    ingredient_mock_2 = MagicMock(spec=Ingredient)

    ingredient_mock_2.get_name.return_value = INGREDIENTS_INFO[1]["ingredient_name"]
    ingredient_mock_2.get_type.return_value = INGREDIENTS_INFO[1]["ingredient_type"]
    ingredient_mock_2.get_price.return_value = INGREDIENTS_INFO[1]["ingredient_price"]

    return ingredient_mock_2

@pytest.fixture
def db():
    return Database()
