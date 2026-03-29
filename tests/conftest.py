import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class IngredientTypes:
    SAUCE = INGREDIENT_TYPE_SAUCE
    FILLING = INGREDIENT_TYPE_FILLING

@pytest.fixture
def test_bun():
    return Bun("Test Bun (dont eat!)", 100)

@pytest.fixture
def test_sauce_ingredient():
    return Ingredient(IngredientTypes.SAUCE, "Souce emulator", 50)

@pytest.fixture
def test_filling():
    return Ingredient(IngredientTypes.FILLING, "Velociraptor meat", 150)

@pytest.fixture
def test_burger(test_bun, test_sauce_ingredient, test_filling):
    burger = Burger()
    burger.set_buns(test_bun)
    burger.add_ingredient(test_sauce_ingredient)
    burger.add_ingredient(test_filling)
    return burger

@pytest.fixture
def empty_burger():
    return Burger()
