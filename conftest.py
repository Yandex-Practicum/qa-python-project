from unittest.mock import Mock

import pytest

import data
from praktikum import ingredient_types


@pytest.fixture()
def mock_bun():
    bun_mock = Mock()
    bun_mock.name = data.BUN_NAME
    bun_mock.price = data.BUN_PRICE
    bun_mock.get_name.return_value = data.BUN_NAME
    bun_mock.get_price.return_value = data.BUN_PRICE
    return bun_mock


@pytest.fixture()
def mock_ingredient():
    ingredient_mock = Mock()
    ingredient_mock.name = data.INGREDIENTS_NAME[0]
    ingredient_mock.price = data.INGREDIENTS_PRICE[0]
    ingredient_mock.type = ingredient_types.INGREDIENT_TYPE_SAUCE
    ingredient_mock.get_name.return_value = data.INGREDIENTS_NAME[0]
    ingredient_mock.get_price.return_value = data.INGREDIENTS_PRICE[0]
    ingredient_mock.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    return ingredient_mock
