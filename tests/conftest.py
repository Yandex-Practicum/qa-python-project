import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.ingredient import Ingredient
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from unittest.mock import MagicMock


@pytest.fixture
def sample_bun():
    return Bun(name="green", price=10)

@pytest.fixture
def bun():
    return Bun("Green Bun", 10)

@pytest.fixture
def burger_with_bun(bun):
    burger = Burger()
    burger.set_buns(bun)
    return burger

@pytest.fixture
def ingredient():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = "pickles"
    ingredient.get_price.return_value = 2
    ingredient.get_type.return_value = "topping"
    return ingredient

@pytest.fixture
def ingredient_2():
    ingredient = MagicMock(spec=Ingredient)
    ingredient.get_name.return_value = "onion"
    ingredient.get_price.return_value = 1
    ingredient.get_type.return_value = "topping"
    return ingredient_2

@pytest.fixture
def buns_data():
    return [
        {"name": "black bun", "price": 100},
        {"name": "white bun", "price": 200},
        {"name": "red bun", "price": 300},
    ]

@pytest.fixture
def ingredient_list_data():
    return [
        {"type": INGREDIENT_TYPE_SAUCE, "name": "hot sauce", "price": 100},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "sour cream", "price": 200},
        {"type": INGREDIENT_TYPE_SAUCE, "name": "chii sauce", "price": 300},
        {"type": INGREDIENT_TYPE_FILLING, "name": "cutlet", "price": 100},
        {"type": INGREDIENT_TYPE_FILLING, "name": "dinosaur", "price": 200},
        {"type": INGREDIENT_TYPE_FILLING, "name": "sausage", "price": 300},
    ]
@pytest.fixture
def database(buns_data, ingredient_list_data):
    db = Database()
    db.buns = [Bun(data["name"], data["price"]) for data in buns_data]
    db.ingredients = [
        Ingredient(data["type"], data["name"], data["price"]) for data in ingredient_list_data
    ]

    return db

@pytest.fixture(params=[
    (INGREDIENT_TYPE_SAUCE, "sour creme", 200),
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 100),
    (INGREDIENT_TYPE_FILLING, "sausage", 300),
])
def ingredient_data(request):
    return request.param