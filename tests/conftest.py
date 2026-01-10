import pytest
from unittest import mock
from Diplom_1.database import Database
from Diplom_1.bun import Bun
from Diplom_1.ingredient import Ingredient
from Diplom_1.burger import Burger
from Diplom_1.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


@pytest.fixture
def bun_fixture():
    return Bun(name="Classic Bun", price=199)


@pytest.fixture
def ingredient_fixture():
    return Ingredient(ingredient_type="Начинки", name="Биокотлета", price=300)


@pytest.fixture
def burger_fixture(bun_fixture, ingredient_fixture):
    burger = Burger()
    burger.set_buns(bun_fixture)
    burger.add_ingredient(ingredient_fixture)
    return burger


@pytest.fixture
def mock_buns():
    return [
        Bun(name="black bun", price=100),
        Bun(name="white bun", price=200),
        Bun(name="red bun", price=300)
    ]


@pytest.fixture
def mock_ingredients():
    return [
        Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="hot sauce", price=100),
        Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="sour cream", price=200),
        Ingredient(ingredient_type=INGREDIENT_TYPE_SAUCE, name="chili sauce", price=300),
        Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="cutlet", price=100),
        Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="dinosaur", price=200),
        Ingredient(ingredient_type=INGREDIENT_TYPE_FILLING, name="sausage", price=300)
    ]


@pytest.fixture
def empty_database():
    with mock.patch.object(Database, '__init__', lambda x: None):
        db = Database()
        db.buns = []
        db.ingredients = []
        return db


@pytest.fixture
def populated_database(mock_buns, mock_ingredients):
    with mock.patch.object(Database, '__init__', lambda x: None):
        db = Database()
        db.buns = mock_buns
        db.ingredients = mock_ingredients
        return db


@pytest.fixture
def database():
    return Database()
