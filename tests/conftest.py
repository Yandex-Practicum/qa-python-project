import pytest

from unittest.mock import Mock

from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types
from data import BUN_NAME, BUN_PRICE, FILLING_NAME, FILLING_PRICE, SAUCE_NAME, SAUCE_PRICE


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture()
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = BUN_NAME
    mock_bun.get_price.return_value = BUN_PRICE
    return mock_bun


@pytest.fixture()
def mock_filling():
    mock_filling = Mock(spec=Ingredient)
    mock_filling.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = FILLING_NAME
    mock_filling.get_price.return_value = FILLING_PRICE
    return mock_filling


@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(spec=Ingredient)
    mock_sauce.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = SAUCE_NAME
    mock_sauce.get_price.return_value = SAUCE_PRICE
    return mock_sauce