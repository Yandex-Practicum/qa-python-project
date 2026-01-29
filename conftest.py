from unittest.mock import Mock
import pytest
from praktikum.database import Database
from praktikum.burger import Burger

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "КосмоБулка"
    mock_bun.get_price.return_value = 55.00
    return mock_bun

@pytest.fixture
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Шницель"
    mock_ingredient.get_price.return_value = 65.00
    mock_ingredient.get_type.return_value = "Начинка"
    return mock_ingredient

@pytest.fixture
def mock_ingredient_next():
    mock_ingredient_next = Mock()
    mock_ingredient_next.get_name.return_value = "Чесночный"
    mock_ingredient_next.get_price.return_value = 20.00
    mock_ingredient_next.get_type.return_value = "Соус"
    return mock_ingredient_next

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def burger():
    return Burger()

