import pytest
from unittest.mock import create_autospec

from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.burger import Burger
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# -------------------------------------------------------------------
# Фикстуры для конкретных объектов (реальные или моки)
# -------------------------------------------------------------------

@pytest.fixture
def black_bun():
    """Реальная булочка black bun."""
    return Bun("black bun", 100)


@pytest.fixture
def white_bun():
    """Реальная булочка white bun."""
    return Bun("white bun", 200)


@pytest.fixture
def red_bun():
    """Реальная булочка red bun."""
    return Bun("red bun", 300)


@pytest.fixture
def hot_sauce():
    """Реальный соус hot sauce."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def sour_cream():
    """Реальный соус sour cream."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)


@pytest.fixture
def chili_sauce():
    """Реальный соус chili sauce."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300)


@pytest.fixture
def cutlet():
    """Реальная начинка cutlet."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)


@pytest.fixture
def dinosaur():
    """Реальная начинка dinosaur."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)


@pytest.fixture
def sausage():
    """Реальная начинка sausage."""
    return Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)


# -------------------------------------------------------------------
# Фикстуры для моков (используются в тестах Burger)
# -------------------------------------------------------------------

@pytest.fixture
def mock_bun():
    """Мок булочки с предопределёнными значениями."""
    bun = create_autospec(Bun, instance=True)
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_ingredient_sauce():
    """Мок соуса."""
    ing = create_autospec(Ingredient, instance=True)
    ing.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ing.get_name.return_value = "hot sauce"
    ing.get_price.return_value = 200
    return ing


@pytest.fixture
def mock_ingredient_filling():
    """Мок начинки."""
    ing = create_autospec(Ingredient, instance=True)
    ing.get_type.return_value = INGREDIENT_TYPE_FILLING
    ing.get_name.return_value = "cutlet"
    ing.get_price.return_value = 300
    return ing


# -------------------------------------------------------------------
# Фикстуры для сложных объектов
# -------------------------------------------------------------------

@pytest.fixture
def database():
    """Экземпляр базы данных."""
    return Database()


@pytest.fixture
def burger():
    """Пустой бургер."""
    return Burger()


@pytest.fixture
def burger_with_bun(burger, mock_bun):
    """Бургер с установленной булкой (мок)."""
    burger.set_buns(mock_bun)
    return burger