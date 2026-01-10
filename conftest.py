import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING
from unittest.mock import Mock


@pytest.fixture(scope="function")
def mock_bun():
    bun_mock = Mock()
    bun_mock.get_name.return_value = "Краторная булка N-200i"
    bun_mock.get_price.return_value = "1255"
    return bun_mock

@pytest.fixture(scope="function")
def mock_ingredients():
    ingredients_mock = Mock()
    ingredients_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredients_mock.get_name.return_value = "Говяжий метеорит (отбивная)"
    ingredients_mock.get_price.return_value = "3000"
    return ingredients_mock