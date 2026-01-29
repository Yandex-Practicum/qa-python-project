from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest

@pytest.fixture
def mock_burger():
    bun = Bun("white", 50)
    ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 20)
    ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)
    burger = Burger()
    burger.set_buns(bun)
    burger.add_ingredient(ingredient1)
    burger.add_ingredient(ingredient2)
    return burger
