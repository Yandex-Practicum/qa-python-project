import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 50
    return bun

@pytest.fixture
def mock_ingredient():
    ing = Mock(spec=Ingredient)
    ing.get_name.return_value = "mock ingredient"
    ing.get_price.return_value = 20
    ing.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ing