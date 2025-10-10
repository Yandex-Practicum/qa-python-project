import random

import pytest
from faker import Faker

from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

fake = Faker("ru_RU")

TEST_BUNS = [
    Bun("black bun", 100),
    Bun("white bun", 200),
    Bun("red bun", 300)
]

TEST_INGREDIENTS = [
    Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    Ingredient(INGREDIENT_TYPE_SAUCE, "sour cream", 200),
    Ingredient(INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
    Ingredient(INGREDIENT_TYPE_FILLING, "cutlet", 100),
    Ingredient(INGREDIENT_TYPE_FILLING, "dinosaur", 200),
    Ingredient(INGREDIENT_TYPE_FILLING, "sausage", 300)
]


@pytest.fixture
def create_bun():
    name = fake.word()
    price = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.0, max_value=100.0), 2)
    return Bun(name=name, price=price)


@pytest.fixture
def create_ingredient(request):
    ingredient_type = request.param
    name = fake.word()
    price = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.0, max_value=100.0), 2)
    return Ingredient(ingredient_type=ingredient_type, name=name, price=price)


@pytest.fixture
def create_random_ingredient():
    def _create():
        ingredient_type = random.choice([INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING])
        name = fake.word()
        price = round(fake.pyfloat(left_digits=2, right_digits=2, positive=True, min_value=1.0, max_value=100.0), 2)
        return Ingredient(ingredient_type=ingredient_type, name=name, price=price)

    return _create


@pytest.fixture
def create_database():
    return Database()


@pytest.fixture
def create_burger():
    return Burger()


@pytest.fixture
def create_burger_with_ingredients(create_burger, create_random_ingredient, request):
    for _ in range(request.param):
        create_burger.add_ingredient(create_random_ingredient())
    return create_burger
