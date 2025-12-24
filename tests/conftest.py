import pytest
from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.database import Database

@pytest.fixture
def empty_burger():
    # Новый бургер без начинки и булки
    return Burger()

@pytest.fixture
def fake_bun():
    # Имитация булочки с нужными параметрами
    bun = Mock()
    bun.get_name.return_value = "test bun"
    bun.get_price.return_value = 123.0
    return bun

@pytest.fixture
def fake_ingredient():
    # Простой ингредиент для тестов (тип, имя, цена задаются в тестах)
    ingr = Mock()
    ingr.get_type.return_value = "FILLING"
    ingr.get_name.return_value = "test filling"
    ingr.get_price.return_value = 77.0
    return ingr

@pytest.fixture
def fresh_db():
    # Отдельная база для каждого теста, чтобы не было побочных эффектов
    return Database()
