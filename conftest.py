import sys                                                                  # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
import os                                                                   # Импорт чтобы запустился тест, либо $env:PYTHONPATH="." pytest tests/ -v
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
import pytest
from unittest.mock import Mock
from source_code.burger import Burger
from source_code.database import Database
from data.data import ORDER_DATA_CORRECT


@pytest.fixture(autouse=True)
def burger():
    return Burger()


@pytest.fixture(autouse=True)
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = ORDER_DATA_CORRECT[0]["bun_name"]
    bun.get_price.return_value = ORDER_DATA_CORRECT[0]["bun_price"]
    return bun


@pytest.fixture(autouse=True)
def mock_ingredient0():
    ingredient = Mock()
    ingredient.get_type.return_value = ORDER_DATA_CORRECT[0]["ingredient_type"]
    ingredient.get_name.return_value = ORDER_DATA_CORRECT[0]["ingredient_name"]
    ingredient.get_price.return_value = ORDER_DATA_CORRECT[0]["ingredient_price"]
    return ingredient


@pytest.fixture(autouse=True)
def mock_ingredient1():
    ingredient = Mock()
    ingredient.get_type.return_value = ORDER_DATA_CORRECT[1]["ingredient_type"]
    ingredient.get_name.return_value = ORDER_DATA_CORRECT[1]["ingredient_name"]
    ingredient.get_price.return_value = ORDER_DATA_CORRECT[1]["ingredient_price"]
    return ingredient


@pytest.fixture(autouse=True)
def dbase():
    return Database()