import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.bun import Bun
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data
from unittest.mock import Mock
@pytest.fixture()
def create_sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE,Data.spicy, Data.price_1)
    return sauce

@pytest.fixture()
def create_filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, Data.protostomia, Data.price_2)
    return filling

@pytest.fixture()
def create_bun():
    bun=Bun(Data.crater_bun, Data.price_3)
    return bun
@pytest.fixture()
def mock_bun(create_bun):
    mock = Mock()
    mock.get.return_value = create_bun
    return mock

@pytest.fixture()
def mock_sauce(create_sauce):
    mock = Mock()
    mock.get.return_value = create_sauce
    return mock

@pytest.fixture()
def mock_filling(create_filling):
    mock = Mock()
    mock.get.return_value = create_filling
    return mock


