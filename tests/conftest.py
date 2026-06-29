import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
import data

@pytest.fixture
def burger():
    """Возвращает чистый экземпляр бургера для каждого теста."""
    return Burger()

@pytest.fixture
def mock_bun():
    """Возвращает мок булочки с настроенными возвращаемыми значениями."""
    bun = Mock()
    bun.get_price.return_value = data.BUN_PRICE
    bun.get_name.return_value = data.BUN_NAME
    return bun

@pytest.fixture
def mock_ingredient():
    """Возвращает мок ингредиента с настроенными возвращаемыми значениями."""
    ingredient = Mock()
    ingredient.get_price.return_value = data.INGREDIENT_PRICE
    ingredient.get_name.return_value = data.INGREDIENT_NAME
    ingredient.get_type.return_value = data.INGREDIENT_TYPE
    return ingredient