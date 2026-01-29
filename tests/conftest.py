import pytest
from unittest.mock import Mock

from data import DataBun, DataIngredient
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING


@pytest.fixture()
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = DataBun.NAME_BUN
    mock.get_price.return_value = DataBun.PRICE_BUN
    return mock

@pytest.fixture()
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_price.return_value = DataIngredient.PRICE_INGREDIENT
    mock.get_name.return_value = DataIngredient.NAME_INGREDIENT
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock

