import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture()
def mock_bun_name_price():
    bun_mock = Mock()
    bun_mock.name = "black bun"
    bun_mock.price = 100
    bun = Bun(bun_mock.name, bun_mock.price)
    return bun

@pytest.fixture()
def mock_ingredient_type_name_price():
    ingredient_mock = Mock()
    ingredient_mock.type = "SAUCE"
    ingredient_mock.name = "hot sauce"
    ingredient_mock.price = 100
    ingredient = Ingredient(ingredient_mock.type, ingredient_mock.name, ingredient_mock.price)
    return ingredient