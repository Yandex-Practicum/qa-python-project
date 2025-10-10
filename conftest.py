import pytest
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_mock():
    mock = Mock()
    mock.get_name.return_value = "Булка"
    mock.get_price.return_value = 100.3
    return mock

@pytest.fixture()
def ingredient_sauce_mock():
    mock = Mock()
    mock.get_price.return_value = 100.3
    mock.get_name.return_value = "Цезарь"
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock

@pytest.fixture()
def ingredient_filling_mock():
    mock = Mock()
    mock.get_price.return_value = 200.3
    mock.get_name.return_value = "Котлета"
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock