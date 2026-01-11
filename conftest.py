import pytest
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

# Фикстуры для булок
@pytest.fixture
def mock_bun():
    return Bun("black bun", 100)

# Фикстуры для ингредиентов
@pytest.fixture
def mock_sauce():
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)

@pytest.fixture
def mock_filling():
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 200)

# Фикстура для подготовленного бургера
@pytest.fixture
def prepared_burger(mock_bun, mock_sauce, mock_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_sauce)
    burger.add_ingredient(mock_filling)
    return burger

@pytest.fixture
def empty_burger():
    return Burger()