import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import TestData


@pytest.fixture
def sample_burger():
    """Фикстура для создания тестового бургера"""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура для мока булочки"""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = TestData.BUN_NAME
    mock.get_price.return_value = TestData.BUN_PRICE
    return mock


@pytest.fixture
def mock_sauce():
    """Фикстура для мока соуса"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = TestData.SAUCE_NAME
    mock.get_price.return_value = TestData.SAUCE_PRICE
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock


@pytest.fixture
def mock_filling():
    """Фикстура для мока начинки"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = TestData.FILLING_NAME
    mock.get_price.return_value = TestData.FILLING_PRICE
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture
def burger_with_ingredients(sample_burger, mock_bun, mock_sauce, mock_filling):
    """Фикстура для бургера с ингредиентами"""
    sample_burger.set_buns(mock_bun)
    sample_burger.add_ingredient(mock_sauce)
    sample_burger.add_ingredient(mock_filling)
    return sample_burger