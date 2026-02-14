# Фикстуры для тестов.

import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from tests.test_constants import (
    BUN_BLACK, PRICE_100,
    INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE
)


@pytest.fixture
def ingredient():
    # Фикстура для создания ингредиента.
    return Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_HOT_SAUCE, PRICE_100)


@pytest.fixture
def bun():
    # Фикстура для создания булочки.
    return Bun(BUN_BLACK, PRICE_100)

