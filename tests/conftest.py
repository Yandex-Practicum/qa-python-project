import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data.ingredients import INGREDIENTS_DATA

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredients():
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_type.return_value = INGREDIENTS_DATA['sauce']['type']
    ingredient1.get_name.return_value = INGREDIENTS_DATA['sauce']['name']
    ingredient1.get_price.return_value = INGREDIENTS_DATA['sauce']['price']

    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_type.return_value = INGREDIENTS_DATA['veggie']['type']
    ingredient2.get_name.return_value = INGREDIENTS_DATA['veggie']['name']
    ingredient2.get_price.return_value = INGREDIENTS_DATA['veggie']['price']

    ingredient3 = Mock(spec=Ingredient)
    ingredient3.get_type.return_value = INGREDIENTS_DATA['meat']['type']
    ingredient3.get_name.return_value = INGREDIENTS_DATA['meat']['name']
    ingredient3.get_price.return_value = INGREDIENTS_DATA['meat']['price']

    return {
        'sauce': ingredient1,
        'veggie': ingredient2,
        'meat': ingredient3,
        'all': [ingredient1, ingredient2, ingredient3]
    }