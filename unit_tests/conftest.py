import sys
import os
from pathlib import Path

# Добавляем корневую директорию в PYTHONPATH
root_dir = str(Path(__file__).parent.parent)
sys.path.insert(0, root_dir)

import pytest
from unittest.mock import Mock
from burger import Burger


@pytest.fixture
def burger():
    """Фикстура для создания бургера"""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки"""
    mock = Mock()
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture
def mock_ingredient_sauce():
    """Фикстура для создания мока соуса"""
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "test sauce"
    mock.get_price.return_value = 50.0
    return mock


@pytest.fixture
def mock_ingredient_filling():
    """Фикстура для создания мока начинки"""
    mock = Mock()
    mock.get_type.return_value = "FILLING"
    mock.get_name.return_value = "test filling"
    mock.get_price.return_value = 75.0
    return mock


@pytest.fixture
def mock_ingredient_extra():
    """Фикстура для создания дополнительного мока ингредиента"""
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "extra sauce"
    mock.get_price.return_value = 25.0
    return mock