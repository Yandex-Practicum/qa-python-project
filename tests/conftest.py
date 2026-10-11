"""
Фикстуры для юнит-тестов.
Все фикстуры собраны здесь, чтобы не дублировать их в файлах тестов.
"""
from unittest.mock import Mock

import pytest

from praktikum.burger import Burger
from praktikum.database import Database
from tests.test_data import (
    BUN_NAME,
    BUN_PRICE,
    SAUCE_TYPE,
    SAUCE_NAME,
    SAUCE_PRICE,
    FILLING_TYPE,
    FILLING_NAME,
    FILLING_PRICE,
)


@pytest.fixture
def burger():
    """Пустой бургер."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Мок булки с фиксированным именем и ценой."""
    bun = Mock()
    bun.get_name.return_value = BUN_NAME
    bun.get_price.return_value = BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce():
    """Мок соуса с фиксированным типом, именем и ценой."""
    sauce = Mock()
    sauce.get_type.return_value = SAUCE_TYPE
    sauce.get_name.return_value = SAUCE_NAME
    sauce.get_price.return_value = SAUCE_PRICE
    return sauce


@pytest.fixture
def mock_filling():
    """Мок начинки с фиксированным типом, именем и ценой."""
    filling = Mock()
    filling.get_type.return_value = FILLING_TYPE
    filling.get_name.return_value = FILLING_NAME
    filling.get_price.return_value = FILLING_PRICE
    return filling


@pytest.fixture
def database():
    """Экземпляр базы данных со стандартным содержимым."""
    return Database()