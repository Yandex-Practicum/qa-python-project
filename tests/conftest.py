import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING


@pytest.fixture
def sample_bun():
    return Bun("test bun", 100)


@pytest.fixture
def sample_sauce():
    return Ingredient(IngredientTypes.SAUCE, "test sauce", 50)


@pytest.fixture
def sample_filling():
    return Ingredient(IngredientTypes.FILLING, "test filling", 150)


@pytest.fixture
def sample_burger(sample_bun, sample_sauce, sample_filling):
    burger = Burger()
    burger.set_buns(sample_bun)
    burger.add_ingredient(sample_sauce)
    burger.add_ingredient(sample_filling)
    return burger


@pytest.fixture
def empty_burger():
    return Burger()
