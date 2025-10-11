import pytest
from unittest.mock import Mock
from ..data import BUNS_DATA, FILLINGS_DATA, SAUSES_DATA


# Фикстура возвращает мок булки
@pytest.fixture
def mock_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = BUNS_DATA[0]["name"]
    bun_mock.get_price.return_value = BUNS_DATA[0]["price"]
    return bun_mock


# Фикстура возвращает мок начинки
@pytest.fixture
def mock_filling():
    filling_mock = Mock()
    filling_mock.get_name.return_value = FILLINGS_DATA[0]["name"]
    filling_mock.get_price.return_value = FILLINGS_DATA[0]["price"]
    filling_mock.get_type.return_value = FILLINGS_DATA[0]["type"]
    return filling_mock


# Фикстура возвращает мок соуса
@pytest.fixture
def mock_sause():
    sause_mock = Mock()
    sause_mock.get_name.return_value = SAUSES_DATA[0]["name"]
    sause_mock.get_price.return_value = SAUSES_DATA[0]["price"]
    sause_mock.get_type.return_value = SAUSES_DATA[0]["type"]
    return sause_mock
