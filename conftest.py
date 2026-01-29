from unittest.mock import Mock
import pytest
from data import DataBun, DataIngredient
from praktikum import ingredient_types
from praktikum.burger import Burger


@pytest.fixture
def burger():
    burger = Burger()

    return burger


@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = DataBun.NAME_BUN
    mock_bun.get_price.return_value = DataBun.PRICE_BUN

    return mock_bun


@pytest.fixture(scope='function')
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.get_price.return_value = DataIngredient.PRICE_SAUCE
    mock_sauce.get_name.return_value = DataIngredient.NAME_SAUCE
    mock_sauce.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE

    return mock_sauce


@pytest.fixture(scope='function')
def mock_filling():
    mock_filling = Mock()
    mock_filling.get_price.return_value = DataIngredient.PRICE_SAUCE
    mock_filling.get_name.return_value = DataIngredient.NAME_FILLING
    mock_filling.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING

    return mock_filling
