import pytest
import allure
from ya_praktikum.bun import Bun
from ya_praktikum.ingredient import Ingredient

@pytest.fixture
@allure.description('Создание булочки')
def create_bun():
    return Bun('Булочка', 100)

@pytest.fixture
@allure.description('Создание ингредиента')
def create_ingredient(ingredient_type, name, price):
    return Ingredient(ingredient_type, name, price)

@pytest.fixture
@allure.description('Создание ингредиента с заданными параметрами')
def create_ing():
    return Ingredient('Соус', 'Сырный', 150)