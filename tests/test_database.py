import pytest

from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.fixture
def database():
    return Database()


def test_available_buns_count(database):
    assert len(database.available_buns()) == 3


def test_available_ingredients_count(database):
    assert len(database.available_ingredients()) == 6


@pytest.mark.parametrize("index, name, price", [
    pytest.param(0, "black bun", 100, id="black"),
    pytest.param(1, "white bun", 200, id="white"),
    pytest.param(2, "red bun", 300, id="red"),
])
def test_available_buns_content(database, index, name, price):
    bun = database.available_buns()[index]

    assert (bun.get_name(), bun.get_price()) == (name, price)


@pytest.mark.parametrize("index, type_, name, price", [
    pytest.param(0, INGREDIENT_TYPE_SAUCE, "hot sauce", 100, id="hot_sauce"),
    pytest.param(1, INGREDIENT_TYPE_SAUCE, "sour cream", 200, id="sour_cream"),
    pytest.param(2, INGREDIENT_TYPE_SAUCE, "chili sauce", 300, id="chili_sauce"),
    pytest.param(3, INGREDIENT_TYPE_FILLING, "cutlet", 100, id="cutlet"),
    pytest.param(4, INGREDIENT_TYPE_FILLING, "dinosaur", 200, id="dinosaur"),
    pytest.param(5, INGREDIENT_TYPE_FILLING, "sausage", 300, id="sausage"),
])
def test_available_ingredients_content(database, index, type_, name, price):
    ingredient = database.available_ingredients()[index]

    assert (ingredient.get_type(), ingredient.get_name(), ingredient.get_price()) == (type_, name, price)
    