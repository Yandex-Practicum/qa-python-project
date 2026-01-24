import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun():
    bun = Bun('булочка', 0.9)
    return bun

@pytest.fixture
def burger():
    burger = Burger()
    return burger

@pytest.fixture(params=[
    (INGREDIENT_TYPE_SAUCE, 'зеленый', 0.5),
    (INGREDIENT_TYPE_FILLING, 'огурчик', 1.2)])
def ingredient(request):
    ingredient_type, name, price = request.param
    return Ingredient(ingredient_type, name, price)
