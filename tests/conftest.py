import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
import praktikum.ingredient_types as ingredient_types


@pytest.fixture
def burger():
    """Фикстура для создания бургера"""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "black bun"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def mock_ingredient_filling():
    """Фикстура для создания мока начинки"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "cutlet"
    mock.get_price.return_value = 100.0
    mock.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture
def mock_ingredient_sauce():
    """Фикстура для создания мока соуса"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "hot sauce"
    mock.get_price.return_value = 100.0
    mock.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def multiple_mock_ingredients():
    """Фикстура для создания нескольких моков ингредиентов"""
    mock1 = Mock(spec=Ingredient)
    mock2 = Mock(spec=Ingredient)
    mock3 = Mock(spec=Ingredient)
    return mock1, mock2, mock3

