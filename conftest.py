import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from data import *

@pytest.fixture()
def bunsandOtherIngredients():
    buns = BunsandOtherIngredients.mock_buns
    ingredients = BunsandOtherIngredients.mock_ingredients
    return[buns, ingredients]
