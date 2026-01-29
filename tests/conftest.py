import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture()
def bun():
    return Bun("black bun", 100)

@pytest.fixture()
def burger():
    return Burger()

@pytest.fixture()
def sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture()
def filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)

@pytest.fixture()
def mock_bun():
    mock_bun = Mock(spec=Bun)
    mock_bun.get_name.return_value = "white bun"
    mock_bun.get_price.return_value = 200
    return mock_bun

@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(spec=Ingredient)
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = "sour cream"
    mock_sauce.get_price.return_value = 200
    return mock_sauce

@pytest.fixture()
def mock_filling():
    mock_filling = Mock(spec=Ingredient)
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = "dinosaur"
    mock_filling.get_price.return_value = 200
    return mock_filling

@pytest.fixture()
def full_burger(mock_bun, mock_sauce, mock_filling):
    full_burger = Burger()
    full_burger.set_buns(mock_bun)
    full_burger.add_ingredient(mock_sauce)
    full_burger.add_ingredient(mock_filling)
    return full_burger

