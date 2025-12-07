from typing import Callable
from unittest.mock import Mock

import pytest

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *
from core.utils import get_bun_mock, get_ingredient_mock


@pytest.fixture
def get_fake_bun() -> Callable:
    def _inner(count: int = 1) -> list[Mock]:
        return [get_bun_mock() for _ in range(count)]

    return _inner


@pytest.fixture
def get_fake_ingredient() -> Callable:
    def _inner(count: int = 1) -> list[Mock]:
        return [get_ingredient_mock() for _ in range(count)]

    return _inner


@pytest.fixture
def get_buns_from_db() -> list[Bun]:
    return [
        Bun("black bun", 100),
        Bun("white bun", 200),
        Bun("red bun", 300),
    ]


@pytest.fixture
def get_ingredients_from_db() -> list[Ingredient]:
    return [
        Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
        Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
        Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
        Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
        Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300),
    ]
