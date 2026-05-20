import pytest
from bun import Bun
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from burger import Burger


@pytest.fixture
def bun():
    """Фикстура: создает булочку для тестов"""
    return Bun("black bun", 100)


@pytest.fixture
def another_bun():
    """Фикстура: создает другую булочку для тестов"""
    return Bun("white bun", 200)


@pytest.fixture
def filling_ingredient():
    """Фикстура: создает ингредиент-начинку"""
    return Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100)


@pytest.fixture
def another_filling_ingredient():
    """Фикстура: создает другой ингредиент-начинку"""
    return Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200)


@pytest.fixture
def sauce_ingredient():
    """Фикстура: создает ингредиент-соус"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)


@pytest.fixture
def another_sauce_ingredient():
    """Фикстура: создает другой ингредиент-соус"""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200)


@pytest.fixture
def burger():
    """Фикстура: создает пустой бургер"""
    return Burger()


@pytest.fixture
def burger_with_bun(burger, bun):
    """Фикстура: создает бургер с булочкой"""
    burger.set_buns(bun)
    return burger


@pytest.fixture
def burger_with_ingredients(burger_with_bun, filling_ingredient, another_filling_ingredient, sauce_ingredient):
    """Фикстура: создает бургер с булочкой и тремя ингредиентами"""
    burger_with_bun.add_ingredient(filling_ingredient)      # cutlet
    burger_with_bun.add_ingredient(another_filling_ingredient)  # dinosaur
    burger_with_bun.add_ingredient(sauce_ingredient)       # hot sauce
    return burger_with_bun
