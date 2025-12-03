"""
Общие фикстуры для всех тестов
"""
import pytest
from unittest.mock import Mock
import sys
import os

# Добавляем текущую директорию в путь для импортов
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

@pytest.fixture
def bun():
    """Фикстура для создания булочки"""
    from bun import Bun
    return Bun("Краторная булочка", 100.0)


@pytest.fixture
def mock_bun():
    """Фикстура для мока булочки"""
    mock = Mock()
    mock.get_price.return_value = 100
    mock.get_name.return_value = "test bun"
    return mock


@pytest.fixture
def ingredient():
    """Фикстура для создания ингредиента"""
    from ingredient import Ingredient
    from ingredient_types import INGREDIENT_TYPE_SAUCE
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100.0)


@pytest.fixture  
def mock_ingredient():
    """Фикстура для мока ингредиента"""
    from ingredient_types import INGREDIENT_TYPE_SAUCE
    mock = Mock()
    mock.get_price.return_value = 50
    mock.get_name.return_value = "test ingredient"
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def burger():
    """Фикстура для создания бургера"""
    from burger import Burger
    return Burger()


@pytest.fixture
def database():
    """Фикстура для создания базы данных"""
    from database import Database
    return Database()