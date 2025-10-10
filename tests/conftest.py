import pytest
from database import Database
from unittest.mock import MagicMock
from burger import Burger




@pytest.fixture
def bun():
    bun_mock = MagicMock()
    bun_mock.get_name.return_value = "Large Bun"
    bun_mock.get_price.return_value = 200.0
    return bun_mock

@pytest.fixture
def ingredient():
    ingredient_mock = MagicMock()
    ingredient_mock.get_name.return_value = "Tomato"
    ingredient_mock.get_type.return_value = "SAUCE"
    ingredient_mock.get_price.return_value = 30.0
    return ingredient_mock



