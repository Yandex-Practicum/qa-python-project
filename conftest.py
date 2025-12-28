import pytest
from Diplom_1.ingredient import Ingredient
from Diplom_1.bun import Bun
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import Data

@pytest.fixture()
def create_sauce():
    sauce = Ingredient(INGREDIENT_TYPE_SAUCE,Data.spicy, Data.price_1)
    return sauce

@pytest.fixture()
def create_filling():
    filling = Ingredient(INGREDIENT_TYPE_FILLING, Data.protostomia, Data.price_2)
    return filling

@pytest.fixture()
def create_bun():
    bun=Bun(Data.crater_bun, Data.price_3)
    return bun



