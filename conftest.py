from unittest.mock import Mock
import pytest

from data import BurgerData
from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = BurgerData.BUN_NAME
    bun.get_price.return_value = BurgerData.BUN_PRICE
    return bun


@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_type.return_value = BurgerData.SAUCE_TYPE
    sauce.get_name.return_value = BurgerData.SAUCE_NAME
    sauce.get_price.return_value = BurgerData.SAUCE_PRICE
    return sauce


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_type.return_value = BurgerData.FILLING_TYPE
    filling.get_name.return_value = BurgerData.FILLING_NAME
    filling.get_price.return_value = BurgerData.FILLING_PRICE
    return filling
