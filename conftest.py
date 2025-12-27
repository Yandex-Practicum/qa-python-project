from unittest.mock import Mock
import allure
import pytest
from praktikum.bun import Bun
from praktikum.burger import Burger
from praktikum.database import Database
from praktikum.ingredient import Ingredient

@allure.step("создали экземпляр класса Bun")
@pytest.fixture(scope="function")
def bun_fixture():
    return Bun(name="булочка", price=1.0)

@allure.step("Создали экземпляр класса Ingredient")
@pytest.fixture(scope="function")
def ingredient_fixture():
    return Ingredient(ingredient_type="sauce", name="горчичный соус", price=0.5)

@allure.step("создали экземпляр класса Burger")
@pytest.fixture(scope="function")
def burger_fixture():
    return Burger()

@allure.step("создали экземпляр класса Database")
@pytest.fixture
def database_fixture():
    db = Database()
    return db

@allure.step("Создаёт мок для булочки")
@pytest.fixture
def mock_bun():
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Классическая булочка"
    bun.get_price.return_value = 1.5
    return bun

@allure.step("Создаёт мок для ингредиента")
@pytest.fixture
def mock_ingredient():
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "летучая начинка"
    ingredient.get_price.return_value = 0.5
    ingredient.get_type.return_value = "начинка"
    return ingredient