import pytest
from data import Data
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture()
def awesome_bun():
    bun = Bun(name=Data.bun.get('name'), price=Data.bun.get('price'))
    return bun


@pytest.fixture()
def awesome_ingredient():
    ingredient = Ingredient(ingredient_type=Data.ingredient.get('type'),
                            name=Data.ingredient.get('name'),
                            price=Data.ingredient.get('price'))
    return ingredient


@pytest.fixture()
def another_awesome_ingredient():
    ingredient = Ingredient(ingredient_type=Data.another_ingredient.get('type'),
                            name=Data.another_ingredient.get('name'),
                            price=Data.another_ingredient.get('price'))
    return ingredient
