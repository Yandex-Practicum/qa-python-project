import pytest
from unittest.mock import Mock

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import (
    INGREDIENT_TYPE_FILLING,
    INGREDIENT_TYPE_SAUCE,
)


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_price.return_value = 100.0
    bun.get_name.return_value = "black bun"
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 50.0
    ingredient.get_name.return_value = "karri_sauce"
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return ingredient


@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_price.return_value = 80.0
    ingredient.get_name.return_value = "meat"
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    return ingredient


@pytest.fixture
def multiple_ingredients():
    ingredients = []

    for i in range(3):
        ingredient = Mock(spec=Ingredient)
        ingredient.get_name.return_value = f"ingredient_{i}"
        ingredient.get_price.return_value = 10.0 * (i + 1)
        ingredient.get_type.return_value = (
            INGREDIENT_TYPE_SAUCE
            if i % 2 == 0
            else INGREDIENT_TYPE_FILLING
        )
        ingredients.append(ingredient)

    return ingredients