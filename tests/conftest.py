import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.database import Database



#Создаем тестовую булку
@pytest.fixture
def simple_bun():
    def _create_bun(name="Простая булка", price=100):
        return Bun(name=name, price=price)
    return _create_bun


@pytest.fixture
def burger():
    return Burger()


#Создаем тестовый ингрединет: соус
@pytest.fixture
def simple_ingredient():
    def _create_ingredient(
        ingredient_type=INGREDIENT_TYPE_SAUCE,
        name="Чесночный соус",
        price=12.0
    ):
        return Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    return _create_ingredient


#Создаем тестовую булку c Моком
@pytest.fixture
def fake_bun():
    mock_bun = Mock()
    mock_bun.get_name.return_value = "Булочка с мОком ахахах"
    mock_bun.get_price.return_value = 28
    return mock_bun


#Создаем тестовый ингридиент с Моком
@pytest.fixture
def fake_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.get_name.return_value = "Фейковая начинка"
    mock_ingredient.get_price.return_value = 12
    mock_ingredient.get_type.return_value = "FILLING"
    return mock_ingredient


@pytest.fixture
def fake_sauce():
    mock = Mock()
    mock.get_name.return_value = "Соус со вкусом фейкоа"
    mock.get_price.return_value = 5
    mock.get_type.return_value = "SAUCE"
    return mock


@pytest.fixture
def clean_data_base():
    return Database()




