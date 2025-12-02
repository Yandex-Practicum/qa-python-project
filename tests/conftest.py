import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
__all__ = ['create_mock_ingredient', 'create_mock_bun']


def create_mock_ingredient(name, ingredient_type, price):
    """Вспомогательная функция для создания mock-ингредиента"""
    ingredient = Mock()
    ingredient.get_name = Mock(return_value=name)
    ingredient.get_type = Mock(return_value=ingredient_type)
    ingredient.get_price = Mock(return_value=price)
    return ingredient

def create_mock_bun(name, price):
    """Вспомогательная функция для создания mock-булки"""
    bun = Mock()
    bun.get_name = Mock(return_value=name)
    bun.get_price = Mock(return_value=price)
    return bun

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def white_bun():
    return create_mock_bun("White Bun", 100.0)

@pytest.fixture
def black_bun():
    return create_mock_bun("Black Bun", 150.0)

@pytest.fixture
def sauce_ingredient():
    return create_mock_ingredient("spicy sauce", INGREDIENT_TYPE_SAUCE, 90.0)

@pytest.fixture
def filling_ingredient():
    return create_mock_ingredient("Cutlet", INGREDIENT_TYPE_FILLING, 100.0)

@pytest.fixture(params=[1, 3, 5, 10])
def ingredient_count(request):
    """Parametrized fixture для количества ингредиентов"""
    return request.param

@pytest.fixture(params=[
    (100.0, [50.0], 250.0),
    (150.0, [50.0, 75.0], 425.0),
    (200.0, [100.0, 100.0, 100.0], 700.0),
])
def price_combinations(request):
    """Parametrized fixture для комбинаций цен"""
    return request.param

@pytest.fixture(params=[(0, 1), (1, 0), (0, 2), (2, 0)])
def move_positions(request):
    """Parametrized fixture для позиций перемещения ингредиентов"""
    return request.param