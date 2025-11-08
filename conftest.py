import pytest
from unittest.mock import Mock


@pytest.fixture
def mock_bun():
    mock = Mock()
    mock.get_name.return_value = "Краторная булка N-200i"
    mock.get_price.return_value = 1255
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock()
    mock.get_name.return_value = "Тестовый ингредиент"
    mock.get_price.return_value = 100
    mock.get_type.return_value = 'FILLING'
    return mock


@pytest.fixture
def sample_burger():
    from praktikum.burger import Burger
    burger = Burger()
    
    bun = Mock()
    bun.get_price.return_value = 1255
    bun.get_name.return_value = "Краторная булка N-200i"
    
    ingredient1 = Mock()
    ingredient1.get_price.return_value = 3000
    ingredient1.get_name.return_value = "Говяжий метеорит (отбивная)"
    ingredient1.get_type.return_value = 'FILLING'
    
    ingredient2 = Mock()
    ingredient2.get_price.return_value = 90
    ingredient2.get_name.return_value = "Соус Spicy-X"
    ingredient2.get_type.return_value = 'SAUCE'
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return burger