import pytest

from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = 'black bun'
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_sauce():
    sauce = Mock(spec=Ingredient)
    sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE.lower()
    sauce.get_name.return_value = 'sour cream'
    sauce.get_price.return_value = 200
    return sauce

@pytest.fixture
def mock_filling():
    filling = Mock(spec=Ingredient)
    filling.get_type.return_value = INGREDIENT_TYPE_FILLING.lower()
    filling.get_name.return_value = 'sausage'
    filling.get_price.return_value = 300
    return filling
