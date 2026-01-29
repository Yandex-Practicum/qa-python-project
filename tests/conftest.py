import pytest
from unittest.mock import Mock
from ..praktikum.bun import Bun
from ..praktikum.burger import Burger
from ..praktikum.ingredient import Ingredient
from ..praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from ..praktikum.database import Database


# Дефолтная булочка
@pytest.fixture()
def bun():
    return Bun("red bun", 300)


# Мок булочка
@pytest.fixture()
def mock_bun():
    mock_bun = Mock(Bun)
    mock_bun.get_name.return_value = "black bun"
    mock_bun.get_price.return_value = 100
    return mock_bun


# Дефолтный бургер
@pytest.fixture()
def burger():
    return Burger()


# Дефолтный соус
@pytest.fixture()
def sauce_ingredient():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


# Мок соус
@pytest.fixture()
def mock_sauce():
    mock_sauce = Mock(Ingredient)
    mock_sauce.get_type.return_value = INGREDIENT_TYPE_SAUCE
    mock_sauce.get_name.return_value = "sour cream"
    mock_sauce.get_price.return_value = 200
    return mock_sauce


# Дефолтная начинка
@pytest.fixture()
def filling_ingredient():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)


# Мок начинка
@pytest.fixture()
def mock_filling():
    mock_filling = Mock(Ingredient)
    mock_filling.get_type.return_value = INGREDIENT_TYPE_FILLING
    mock_filling.get_name.return_value = "dinosaur"
    mock_filling.get_price.return_value = 200
    return mock_filling


# Дефолтная БД
@pytest.fixture()
def database():
    return Database()
