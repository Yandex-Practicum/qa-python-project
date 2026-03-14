import pytest
from praktikum.burger import Burger
from praktikum.database import Database


# фикстура создания экземпляра класса Burger
@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def database():
    return Database()

@pytest.fixture
def expected_ingredients():
    return [(ingredient.type, ingredient.name, ingredient.price) for ingredient in Database().available_ingredients()]
