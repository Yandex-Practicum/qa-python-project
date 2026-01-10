from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture(scope='function')
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Флюоресцентная булка R2-D3"
    bun.get_price.return_value = 988
    return bun


@pytest.fixture(scope='function')
def mock_ingredients():
    fill = Mock()
    fill.get_price.return_value = 150
    fill.get_name.return_value = 'Космическая котлета'
    fill.get_type.return_value = INGREDIENT_TYPE_FILLING
    return fill