import pytest
from unittest.mock import Mock

@pytest.fixture
def multiple_mock_ingredients():
    ingredient1 = Mock(spec='Ingredient')
    ingredient1.get_name = Mock(return_value='Соус')
    ingredient1.get_price = Mock(return_value=15.0)
    ingredient1.get_type = Mock(return_value='Фирменный')

    
    ingredient2 = Mock(spec='Ingredient')
    ingredient2.get_name = Mock(return_value='Начинка')
    ingredient2.get_price = Mock(return_value=300.0)
    ingredient2.get_type = Mock(return_value='Отбивная')

    ingredient3 = Mock(spec='Ingredient')
    ingredient3.get_name = Mock(return_value='Начинка2')
    ingredient3.get_price = Mock(return_value=400.0)
    ingredient3.get_type = Mock(return_value='Котлета')
    return ingredient1, ingredient2, ingredient3

@pytest.fixture
def bun_mock():
    bun = Mock(spec='Bun')
    bun.get_name = Mock(return_value='Булка')
    bun.get_price = Mock(return_value=900.0)
    bun.get_type = Mock(return_value='Космическая')
    return bun
