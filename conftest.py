import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def mock_bun():
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "Краторная булка N-200i"
    mock.get_price.return_value = 1255
    return mock


@pytest.fixture
def mock_ingredient():
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "Тестовый ингредиент"
    mock.get_price.return_value = 100
    mock.get_type.return_value = INGREDIENT_TYPE_FILLING
    return mock


@pytest.fixture
def sample_burger():
    from praktikum.burger import Burger
    burger = Burger()
    
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 1255
    bun.get_name.return_value = "Краторная булка N-200i"
    
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_price.return_value = 3000
    ingredient1.get_name.return_value = "Говяжий метеорит (отбивная)"
    ingredient1.get_type.return_value = INGREDIENT_TYPE_FILLING
    
    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_price.return_value = 90
    ingredient2.get_name.return_value = "Соус Spicy-X"
    ingredient2.get_type.return_value = INGREDIENT_TYPE_SAUCE
    
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    
    return burger