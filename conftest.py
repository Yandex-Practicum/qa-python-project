import pytest
from unittest.mock import Mock
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "red bun"
    mock_bun.get_price.return_value = 300
    return mock_bun

@pytest.fixture
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.get_type.return_value = "FILLING"
    mock_ingredient_1.get_name.return_value = "dinosaur"
    mock_ingredient_1.get_price.return_value = 200
    return mock_ingredient_1

@pytest.fixture
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.get_type.return_value = "SAUCE"
    mock_ingredient_2.get_name.return_value = "hot sauce"
    mock_ingredient_2.get_price.return_value = 200
    return mock_ingredient_2