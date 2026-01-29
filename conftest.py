import allure
import pytest
from unittest.mock import Mock
from data import MakeBurger as mb


@allure.title('Создаем мок булки')
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = mb.BUN_NAME
    mock_bun.price = mb.BUN_PRICE
    mock_bun.return_value.get_name = mb.BUN_NAME
    mock_bun.return_value.get_price = mb.BUN_PRICE
    return mock_bun

@allure.title('Создаем мок соуса')
@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = mb.SAUSE_TYPE
    mock_sauce.name = mb.SAUSE_NAME
    mock_sauce.price = mb.SAUSE_PRICE
    mock_sauce.return_value.get_type = mb.SAUSE_TYPE
    mock_sauce.return_value.get_name = mb.SAUSE_NAME
    mock_sauce.return_value.get_price = mb.SAUSE_PRICE
    return mock_sauce

@allure.title('Создаем мок начинки')
@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = mb.FILLING_TYPE
    mock_filling.name = mb.FILLING_NAME
    mock_filling.price = mb.FILLING_PRICE
    mock_filling.return_value.get_type = mb.FILLING_TYPE
    mock_filling.return_value.get_name = mb.FILLING_NAME
    mock_filling.return_value.get_price = mb.FILLING_PRICE
    return mock_filling
