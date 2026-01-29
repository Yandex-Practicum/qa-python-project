from unittest.mock import Mock
import pytest
from data import BurgerData
from database import Database


@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = BurgerData.BUN_NAME
    mock_bun.get_name.return_value = BurgerData.BUN_NAME
    mock_bun.price = BurgerData.BUN_PRICE
    mock_bun.get_price.return_value = BurgerData.BUN_PRICE
    return mock_bun


@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = BurgerData.INGREDIENT_TYPE_SAUCE
    mock_sauce.get_type.return_value = BurgerData.INGREDIENT_TYPE_SAUCE
    mock_sauce.name = BurgerData.SAUCE_NAME
    mock_sauce.get_name.return_value = BurgerData.SAUCE_NAME
    mock_sauce.price = BurgerData.SAUCE_PRICE
    mock_sauce.get_price.return_value = BurgerData.SAUCE_PRICE
    return mock_sauce


@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = BurgerData.INGREDIENT_TYPE_FILLING
    mock_filling.get_type.return_value = BurgerData.INGREDIENT_TYPE_FILLING
    mock_filling.name = BurgerData.FILLING_NAME
    mock_filling.get_name.return_value = BurgerData.FILLING_NAME
    mock_filling.price = BurgerData.FILLING_PRICE
    mock_filling.get_price.return_value = BurgerData.FILLING_PRICE
    return mock_filling


@pytest.fixture
def database():
    return Database()
