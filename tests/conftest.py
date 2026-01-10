import pytest
from unittest.mock import Mock
from diplom_1.praktikum.burger import Burger
from diplom_1.praktikum.database import Database

# Фикстуры для мок-объектов
@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "Краторная булочка"
    mock.get_price.return_value = 100
    return mock

@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_type.return_value = "SAUCE"
    mock.get_name.return_value = "Острый соус"
    mock.get_price.return_value = 50
    return mock

# Фикстура для бургера с ингредиентами
@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger


