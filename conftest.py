import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from data import data_for_ingredient_sauce, data_for_ingredient_filling
from praktikum.ingredient import Ingredient
from praktikum.bun import Bun
import pytest
import data

@pytest.fixture()
def create_bun():
    bun = Bun(data.data_for_bun['name'], data.data_for_bun['price'])
    return bun


@pytest.fixture(params=[data_for_ingredient_sauce, data_for_ingredient_filling])
def create_ingredient(request):
    ingredient_data = request.param
    return Ingredient(ingredient_data['ingredient_type'], ingredient_data['name'], ingredient_data['price'])
