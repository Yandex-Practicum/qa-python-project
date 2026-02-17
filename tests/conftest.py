import pytest
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from unittest.mock import Mock

@pytest.fixture()
def create_burger():
    return Burger()

@pytest.fixture()
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "Crazy bun"
    mock.get_price.return_value = 666
    return mock

@pytest.fixture()
def mock_ingredient():
    mock = Mock()
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_name.return_value = "Crazy ham"
    mock.get_price.return_value = 999
    return mock
