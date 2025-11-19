import pytest
from data import *
from unittest.mock import Mock

@pytest.fixture(scope='function', params=buns_name_price)
def mock_bun(request):
    name, price = request.param
    mock_bun = Mock()
    mock_bun.name = name
    mock_bun.price = price
    return mock_bun

@pytest.fixture(scope='function', params=ingredients_type_name_price)
def mock_ingredient(request):
    ingredient_type, ingredient_name, ingredient_price = request.param
    ingredient = Mock()
    ingredient.type = ingredient_type
    ingredient.name = ingredient_name
    ingredient.price = ingredient_price
    return ingredient
