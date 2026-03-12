import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
import praktikum.ingredient_types as ing_type


from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger


@pytest.fixture
def bun():
    mock_bun = Mock(spec_set=Bun)
    mock_bun.get_name.return_value = 'black bun'
    mock_bun.get_price.return_value = 100
    return mock_bun

@pytest.fixture
def ingredient_filling():
    mock_ingridient = Mock(spec_set=Ingredient)
    mock_ingridient.get_name.return_value = 'cutlet'
    mock_ingridient.get_price.return_value = 100
    mock_ingridient.get_type.return_value = ing_type.INGREDIENT_TYPE_FILLING
    return mock_ingridient

@pytest.fixture
def ingredient_sauce():
    mock_ingridient = Mock(spec_set=Ingredient)
    mock_ingridient.get_name.return_value = 'chili sauce'
    mock_ingridient.get_price.return_value = 300
    mock_ingridient.get_type.return_value = ing_type.INGREDIENT_TYPE_SAUCE
    return mock_ingridient

@pytest.fixture
def burger():
    return Burger()