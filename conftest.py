import pytest
from unittest.mock import Mock
from burger import Burger



@pytest.fixture
def burger():
    burger = Burger()
    return burger


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "white bun"
    mock.get_price.return_value = 200
    return mock


@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100
    mock.get_type.return_value = "SAUCE"
    return mock


@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_name.return_value = "sausage"
    mock.get_price.return_value = 300
    mock.get_type.return_value = "FILLING"
    return mock

@pytest.fixture
def mock_burger():
    mock = Mock()
    mock.bun = ("white bun", 200)
    mock.ingredients = [("SAUCE", "hot sauce", 100), ("FILLING", "sausage", 300)]
    return mock
