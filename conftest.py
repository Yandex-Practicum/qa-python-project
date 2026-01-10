import pytest
from unittest.mock import Mock

from Diplom_1.data import BUN_DATA, INGREDIENT_DATA, INGREDIENT_DATA_1


@pytest.fixture
def bun_mock():
    mock_bun = Mock()
    mock_bun.name = BUN_DATA['name']
    mock_bun.price = BUN_DATA['price']
    mock_bun.get_price.return_value = BUN_DATA['price']
    mock_bun.get_name.return_value = BUN_DATA['name']
    return mock_bun

@pytest.fixture
def ingredient_mock():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_DATA.get('type')
    mock_ingredient.name = INGREDIENT_DATA.get('name')
    mock_ingredient.price = INGREDIENT_DATA.get('price')
    mock_ingredient.get_type.return_value = INGREDIENT_DATA.get('type')
    mock_ingredient.get_name.return_value = INGREDIENT_DATA.get('name')
    mock_ingredient.get_price.return_value = INGREDIENT_DATA.get('price')
    return mock_ingredient

@pytest.fixture
def ingredient_mock_1():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_DATA_1.get('type')
    mock_ingredient.name = INGREDIENT_DATA_1.get('name')
    mock_ingredient.price = INGREDIENT_DATA_1.get('price')
    mock_ingredient.get_type.return_value = INGREDIENT_DATA_1.get('type')
    mock_ingredient.get_name.return_value = INGREDIENT_DATA_1.get('name')
    mock_ingredient.get_price.return_value = INGREDIENT_DATA_1.get('price')
    return mock_ingredient