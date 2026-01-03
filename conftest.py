import sys, os
print("CWD", os.getcwd())
print("PATH before:", sys.path[0])


import pytest
import random
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
import praktikum.ingredient_types as it
from helpers import GenerateData



@pytest.fixture
def bun_creation():
    name = GenerateData.generate_string(7)
    price = GenerateData.generate_num()
    bun = Bun(name, price)
    return bun



@pytest.fixture
def ingredient_creation():
    ingredient_type = random.choice([it.INGREDIENT_TYPE_FILLING, it.INGREDIENT_TYPE_SAUCE])
    price = GenerateData.generate_num()
    name = GenerateData.generate_string(7)
    ingredient = Ingredient(ingredient_type, name, price)
    return ingredient

    
