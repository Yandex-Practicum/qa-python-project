import pytest
from praktikum.bun import Bun
from data import BunData, IngredientData
from praktikum.ingredient import Ingredient
from praktikum import ingredient_types


@pytest.fixture()
def set_data_bun():
    bun = Bun(BunData.bun_name, BunData.bun_price)

    return bun


@pytest.fixture()
def set_data_ingredient():
    ingredient = Ingredient(ingredient_types.INGREDIENT_TYPE_FILLING,
                            IngredientData.ingredient_name, IngredientData.ingredient_price)

    return ingredient
