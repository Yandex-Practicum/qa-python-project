import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture(scope='function')
def mock_bun():
    """Фикстура для мока булочки"""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "Краторная булка N-200i"
    mock.get_price.return_value = 100.0
    return mock


@pytest.fixture(scope='function')
def mock_ingredient_sauce():
    """Фикстура для мока ингредиента-соуса"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "Соус Spicy-X"
    mock.get_type.return_value = "SAUCE"
    mock.get_price.return_value = 90.0
    return mock


@pytest.fixture(scope='function')
def mock_ingredient_filling():
    """Фикстура для мока ингредиента-начинки"""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "Мясо бессмертных моллюсков Protostomia"
    mock.get_type.return_value = "FILLING"
    mock.get_price.return_value = 200.0
    return mock


@pytest.fixture(scope='function')
def burger():
    """Фикстура для создания пустого бургера"""
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture(scope='function')
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    """Фикстура для бургера с булочкой и ингредиентами"""
    from praktikum.burger import Burger
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger
