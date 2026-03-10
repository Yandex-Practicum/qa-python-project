import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


BLACK_BUN = Bun("black bun", 100)
WHITE_BUN = Bun("white bun", 200)
RED_BUN = Bun("red bun", 300)
HOT_SAUCE = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
CUTLET = Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)


@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "hot sauce"
    ingredient.get_price.return_value = 100
    return ingredient


@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
    ingredient.get_name.return_value = "cutlet"
    ingredient.get_price.return_value = 100
    return ingredient


@pytest.fixture
def burger_with_mocks(mock_bun, mock_ingredient_sauce):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    return burger


@pytest.fixture
def empty_burger():
    return Burger()
