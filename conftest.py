import pytest
from unittest.mock import Mock
import praktikum.ingredient_types as IT

@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = "name_bun"
    mock_bun.price = 100

    mock_bun.get_price.return_value = mock_bun.price ## цена 1 булки/ в бургере их 2
    mock_bun.get_name.return_value = mock_bun.name

    yield mock_bun

@pytest.fixture
def mock_ingredient_1():
    mock_ingredient_1 = Mock()
    mock_ingredient_1.type = IT.INGREDIENT_TYPE_FILLING
    mock_ingredient_1.name = "name_ingredient_1"
    mock_ingredient_1.price = 20

    mock_ingredient_1.get_price.return_value = mock_ingredient_1.price
    mock_ingredient_1.get_type.return_value = mock_ingredient_1.type
    mock_ingredient_1.get_name.return_value = mock_ingredient_1.name

    yield mock_ingredient_1

@pytest.fixture
def mock_ingredient_2():
    mock_ingredient_2 = Mock()
    mock_ingredient_2.type = IT.INGREDIENT_TYPE_SAUCE
    mock_ingredient_2.name = "name_ingredient_2"
    mock_ingredient_2.price = 30

    mock_ingredient_2.get_price.return_value = mock_ingredient_2.price
    mock_ingredient_2.get_type.return_value = mock_ingredient_2.type
    mock_ingredient_2.get_name.return_value = mock_ingredient_2.name

    yield mock_ingredient_2    

