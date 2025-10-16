import pytest
from unittest.mock import MagicMock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_sauce():
    # Создаю мок-объект соуса с тестовыми значениями имени, цены и типа
    sauce_mock = MagicMock(spec=Ingredient)
    sauce_mock.get_name.return_value = "test sauce"
    sauce_mock.get_price.return_value = 50
    sauce_mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return sauce_mock

@pytest.fixture
def mock_bun():
    bun = MagicMock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient():
    ingredient = MagicMock()
    ingredient.get_type.return_value = "sauce"
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50
    return ingredient

@pytest.fixture
def mock_filling():
    # Создаю мок-объект начинки с тестовыми значениями имени, цены и типа
    filling_mock = MagicMock(spec=Ingredient)
    filling_mock.get_name.return_value = "test filling"
    filling_mock.get_price.return_value = 150
    filling_mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return filling_mock
