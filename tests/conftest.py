from unittest.mock import Mock

import pytest as pytest

from data import DataBun, DataIngredient


@pytest.fixture()
def mock_bun():
    mock_bun = Mock()
    name, price = DataBun.get_data_bun()
    mock_bun.get_name.return_value = name
    mock_bun.get_price.return_value = price
    return mock_bun


@pytest.fixture()
def mocks_ingredients():
    mocks_ingredients = []
    for _ in range(4):
        mock_ingredient = Mock()
        name, price, type_ingredient = DataIngredient.get_data_ingredient()
        mock_ingredient.get_name.return_value = name
        mock_ingredient.get_price.return_value = price
        mock_ingredient.get_type.return_value = type_ingredient
        mocks_ingredients.append(mock_ingredient)
    return mocks_ingredients

