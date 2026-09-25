from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_SAUCE,
    INGREDIENT_TYPE_FILLING,
)



@pytest.fixture
def burger() -> Burger:
    return Burger()


@pytest.fixture
def database() -> Database:
    return Database()


@pytest.fixture
def real_bun() -> Bun:
    return Bun("black bun", 100)


@pytest.fixture
def real_ingredient() -> Ingredient:
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)



@pytest.fixture
def mock_bun() -> Mock:
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient() -> Mock:
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 50.0
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture
def mock_filling() -> Mock:
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100.0
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


@pytest.fixture
def make_mock_ingredient():
    def _make(price: float = 100.0,
              name: str = "ingredient",
              ingredient_type: str = INGREDIENT_TYPE_SAUCE) -> Mock:
        ingredient = Mock(spec=Ingredient)
        ingredient.get_price.return_value = price
        ingredient.get_name.return_value = name
        ingredient.get_type.return_value = ingredient_type
        return ingredient

    return _make