import allure
import pytest
from unittest.mock import Mock

from burger import Burger
from data import BurgerGetPrice as p, BurgerInfo as b


@allure.title('Создаем мок булки')
@pytest.fixture
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = b.BUN_NAME
    mock_bun.price = b.BUN_PRICE
    mock_bun.return_value.get_name = b.BUN_NAME
    mock_bun.return_value.get_price = b.BUN_PRICE
    return mock_bun


@allure.title('Создаем мок булки 2')
@pytest.fixture
def mock_bun2():
    mock_bun = Mock()
    mock_bun.name = b.BUN2_NAME
    mock_bun.price = b.BUN2_PRICE
    mock_bun.return_value.get_name = b.BUN2_NAME
    mock_bun.return_value.get_price = b.BUN2_PRICE
    return mock_bun


@allure.title('Создаем мок соуса')
@pytest.fixture
def mock_sauce():
    mock_sauce = Mock()
    mock_sauce.type = b.SAUCE_TYPE
    mock_sauce.name = b.SAUCE_NAME
    mock_sauce.price = b.SAUCE_PRICE
    mock_sauce.return_value.get_type = b.SAUCE_TYPE
    mock_sauce.return_value.get_name = b.SAUCE_NAME
    mock_sauce.return_value.get_price = b.SAUCE_PRICE
    return mock_sauce


@allure.title('Создаем мок начинки')
@pytest.fixture
def mock_filling():
    mock_filling = Mock()
    mock_filling.type = b.FILLING_TYPE
    mock_filling.name = b.FILLING_NAME
    mock_filling.price = b.FILLING_PRICE
    mock_filling.return_value.get_type = b.FILLING_TYPE
    mock_filling.return_value.get_name = b.FILLING_NAME
    mock_filling.return_value.get_price = b.FILLING_PRICE
    return mock_filling

@allure.title('Создаем бургер с 6 мок-ингредиентами')
@pytest.fixture
def get_burger_with_6_ingredients(mock_sauce, mock_filling):
    # создаем бургер
    burger = Burger()
    # добавляем 3 соуса
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_sauce)
    # добавляем 3 начинки
    burger.add_ingredient(mock_filling)
    burger.add_ingredient(mock_filling)
    burger.add_ingredient(mock_filling)
    # возвращаем бургер
    return burger


