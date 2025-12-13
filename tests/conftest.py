"""Фикстуры для тестов"""
import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.database import Database

"""Фикстура для создания пустого бургера"""
@pytest.fixture
def empty_burger():
    return Burger()

"""Фикстура для создания бургера с булочкой"""
@pytest.fixture
def burger_with_bun(mock_bun):
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger

"""Фикстура для создания бургера с булочкой и ингредиентами"""
@pytest.fixture
def burger_with_ingredients(mock_bun, mock_ingredient_sauce, mock_ingredient_filling):
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient_sauce)
    burger.add_ingredient(mock_ingredient_filling)
    return burger

"""Фикстура для создания мока булочки"""
@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "Test Bun"
    bun.get_price.return_value = 100.0
    return bun

"""Фикстура для создания мока соуса"""
@pytest.fixture
def mock_ingredient_sauce():
    ingredient = Mock()
    ingredient.get_type.return_value = "SAUCE"
    ingredient.get_name.return_value = "Test Sauce"
    ingredient.get_price.return_value = 50.0
    return ingredient

"""Фикстура для создания мока начинки"""
@pytest.fixture
def mock_ingredient_filling():
    ingredient = Mock()
    ingredient.get_type.return_value = "FILLING"
    ingredient.get_name.return_value = "Test Filling"
    ingredient.get_price.return_value = 80.0
    return ingredient

"""Фикстура для создания базы данных"""
@pytest.fixture
def database():
    return Database()