import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
@pytest.fixture  # фикстура, которая создаёт инградиент - начинку
def ingredient_filling():
    ingredient_filling = [INGREDIENT_TYPE_FILLING, "bacon", 50.45]
    return ingredient_filling

@pytest.fixture  # фикстура, которая создаёт инградиент - соус
def ingredient_sous():
    ingredient_sous = [INGREDIENT_TYPE_SAUCE, "catchup", 40.55]
    return ingredient_sous
