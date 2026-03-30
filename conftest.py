# conftest.py
import pytest
from unittest.mock import Mock
from burger import Burger, Bun, Ingredient
import test_data as td

@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = td.BUN_NAME
    bun.get_price.return_value = td.BUN_PRICE
    return bun

@pytest.fixture
def mock_ingredients():
    ingredient1 = Mock(spec=Ingredient)
    ingredient1.get_type.return_value = td.INGREDIENT_SAUCE_TYPE
    ingredient1.get_name.return_value = td.INGREDIENT_SAUCE_NAME
    ingredient1.get_price.return_value = td.INGREDIENT_SAUCE_PRICE

    ingredient2 = Mock(spec=Ingredient)
    ingredient2.get_type.return_value = td.INGREDIENT_FILLING_TYPE
    ingredient2.get_name.return_value = td.INGREDIENT_FILLING_NAME
    ingredient2.get_price.return_value = td.INGREDIENT_FILLING_PRICE
    
    return [ingredient1, ingredient2]
