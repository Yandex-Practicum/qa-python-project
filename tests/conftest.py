import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun




@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.name = 'bun1'
    mock.price = 1000
    mock.get_name.return_value = 'bun1'
    mock.get_price.return_value = 1000
    return mock

@pytest.fixture
def mock_ingredient():#Фикстура для Ingredient get_price, get_type, get_name
    mock = Mock()
    mock.ingredient_type = 'Начинка'
    mock.name = 'Медвежатина'
    mock.price = 1000
    mock.get_price.return_value = 1000
    mock.get_type.return_value = 'Начинка'
    mock.get_name.return_value = 'Медвежатина'
    return mock

@pytest.fixture
def burger_with_definite_bun() -> Burger: #Фикстура для создания burger с определенным bun
    burger = Burger()
    bun = Bun("black bun", 100.)
    burger.set_buns(bun)
    return burger















