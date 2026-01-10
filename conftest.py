import pytest

from practicum.bun import Bun
from practicum.burger import Burger
from practicum.database import Database
from practicum.ingredient import Ingredient


@pytest.fixture
def bun(request):
    name, price = request.param
    yield Bun(name=name, price=price)


@pytest.fixture
def ingredient(request):
    ingredient_type, name, price = request.param
    yield Ingredient(ingredient_type=ingredient_type, name=name, price=price)


@pytest.fixture(scope="class")
def db():
    yield Database()


@pytest.fixture
def burger():
    yield Burger()


@pytest.fixture
def two_indegrients():
    yield Ingredient("Тип", "Имя", 100), Ingredient("Тип", "Имя", 100)
