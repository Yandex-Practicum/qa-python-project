"""
Фикстуры для тестов
"""
import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data.test_data import (
    BUN_NAME, BUN_PRICE, BUN_NAME_2, BUN_PRICE_2,
    INGREDIENT_NAME, INGREDIENT_PRICE, INGREDIENT_NAME_2, INGREDIENT_PRICE_2
)


@pytest.fixture
def burger_with_bun():
    """Фикстура для создания бургера с булочкой"""
    bun = Bun(BUN_NAME, BUN_PRICE)
    burger = Burger()
    burger.set_buns(bun)
    return burger


@pytest.fixture
def burger_with_ingredients():
    """Фикстура для создания бургера с булочкой и ингредиентами"""
    bun = Bun(BUN_NAME, BUN_PRICE)
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_NAME, INGREDIENT_PRICE)
    ingredient_filling = Ingredient(INGREDIENT_TYPE_FILLING, INGREDIENT_NAME_2, INGREDIENT_PRICE_2)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient)
    burger.add_ingredient(ingredient_filling)
    return burger 