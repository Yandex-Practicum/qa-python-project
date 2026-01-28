import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.data import BunData, IngredientData


@pytest.fixture()
def set_data_bun():
    bun = Bun(BunData.bun_name, BunData.bun_price)
    return bun


@pytest.fixture()
def set_data_ingredient():
    ingredient_1 = Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name=IngredientData.ingredient_name, price=IngredientData.ingredient_price)
    ingredient_2 = Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING,
                              name=IngredientData.ingredient_name, price=IngredientData.ingredient_price)

    return [ingredient_1, ingredient_2]