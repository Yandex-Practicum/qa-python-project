import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "TestBun2000"
    mock.get_price.return_value = 1.0
    return mock


@pytest.fixture
def mock_sauce():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "TestSauce"
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock.get_price.return_value = 1.0
    return mock


@pytest.fixture
def mock_filling():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "TestFilling"
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock.get_price.return_value = 1.0
    return mock


@pytest.fixture
def burger():
    return Burger()
