import pytest
import allure
from unittest.mock import Mock
from praktikum.burger import Burger
from data import BUN_NAME, BUN_PRICE, SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE, FILLING_TYPE, FILLING_NAME, FILLING_PRICE


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = BUN_NAME
    mock.get_price.return_value = BUN_PRICE
    return mock


@pytest.fixture
def mock_sauce():
    mock = Mock()
    mock.get_type.return_value = SAUCE_TYPE
    mock.get_name.return_value = SAUCE_NAME
    mock.get_price.return_value = SAUCE_PRICE
    return mock


@pytest.fixture
def mock_filling():
    mock = Mock()
    mock.get_type.return_value = FILLING_TYPE
    mock.get_name.return_value = FILLING_NAME
    mock.get_price.return_value = FILLING_PRICE
    return mock


@pytest.fixture
def create_mock_bun():
    def _create_mock_bun(name=BUN_NAME, price=BUN_PRICE):
        mock = Mock()
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock

    return _create_mock_bun


@pytest.fixture
def create_mock_ingredient():
    def _create_mock_ingredient(type=SAUCE_TYPE, name=SAUCE_NAME, price=SAUCE_PRICE):
        mock = Mock()
        mock.get_type.return_value = type
        mock.get_name.return_value = name
        mock.get_price.return_value = price
        return mock

    return _create_mock_ingredient


class TestBurger:
    @allure.title('Добавление булочки в бургер')
    def test_set_buns(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    @allure.title('Добавление ингредиентов в бургер')
    @pytest.mark.parametrize('ingredient_type', [SAUCE_TYPE, FILLING_TYPE])
    def test_add_ingredient(self, ingredient_type, create_mock_ingredient):
        mock_ingredient = create_mock_ingredient(type=ingredient_type)
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[-1] == mock_ingredient

    @allure.title('Удаление ингредиента из бургера')
    def test_remove_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.remove_ingredient(0)
        assert burger.ingredients == [mock_filling]

    @allure.title('Перемещение ингредиента в бургере')
    def test_move_ingredient(self, mock_sauce, mock_filling):
        burger = Burger()
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_filling, mock_sauce]

    @allure.title('Расчет стоимости бургера')
    def test_get_price(self, mock_bun, mock_sauce, mock_filling):
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)
        expected_price = (mock_bun.get_price.return_value * 2 +
                          mock_sauce.get_price.return_value +
                          mock_filling.get_price.return_value)
        assert burger.get_price() == expected_price

    @allure.title('Формирование чека')
    def test_get_receipt(self, create_mock_bun, create_mock_ingredient):
        mock_bun = create_mock_bun(BUN_NAME, BUN_PRICE)
        mock_sauce = create_mock_ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        mock_filling = create_mock_ingredient(FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_sauce)
        burger.add_ingredient(mock_filling)

        actual_price = (mock_bun.get_price.return_value * 2 +
                        mock_sauce.get_price.return_value +
                        mock_filling.get_price.return_value)

        expected_receipt = (f'(==== {BUN_NAME} ====)\n'
                            f'= {SAUCE_TYPE.lower()} {SAUCE_NAME} =\n'
                            f'= {FILLING_TYPE.lower()} {FILLING_NAME} =\n'
                            f'(==== {BUN_NAME} ====)\n'
                            f'\n'
                            f'Price: {actual_price}')
        assert burger.get_receipt() == expected_receipt
