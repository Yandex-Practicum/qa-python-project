import pytest

from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = 'black bun'
    mock.get_price.return_value = 100
    return mock

@pytest.fixture
def mock_ingredient_1():
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE.lower()
    mock.get_name.return_value = 'sour cream'
    mock.get_price.return_value = 200
    return mock

@pytest.fixture
def mock_ingredient_2():
    mock = Mock(spec=Ingredient)
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING.lower()
    mock.get_name.return_value = 'sausage'
    mock.get_price.return_value = 300
    return mock