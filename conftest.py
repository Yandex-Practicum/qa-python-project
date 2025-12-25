import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

# мок булочки с методами и атрибутами
@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.configure_mock(name = 'Розовая булочка', price = 199.5)
    bun.get_price.return_value = 199.5
    bun.get_name.return_value = 'Розовая булочка'
    return bun

# мок ингредиента (начинка) с методами и атрибутами
@pytest.fixture
def mock_filling_ingredient():
    ingredient = Mock()
    ingredient.configure_mock(name = 'Котлетка', type = INGREDIENT_TYPE_FILLING, price = 79.5 )
    ingredient.get_price.return_value = 79.5
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = 'Котлетка'
    return ingredient

# мок ингредиента (соус)
@pytest.fixture
def mock_sauce_ingredient():
    ingredient = Mock()
    ingredient.configure_mock(name='Сырный соус', type=INGREDIENT_TYPE_SAUCE, price=79.5)
    ingredient.get_price.return_value = 49.5
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = 'Сырный соус'
    return ingredient

# экземпляр бургера
@pytest.fixture
def real_burger():
    return Burger()

# экземпляр булочки
@pytest.fixture
def real_bun():
    return Bun('Big bun', 199.5)

@pytest.fixture
def db():
    return Database()
