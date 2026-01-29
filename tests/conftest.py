# conftest.py

import pytest
from unittest.mock import Mock
from bun import Bun
from burger import Burger
from ingredient import Ingredient
from database import Database

# Основные фикстуры
@pytest.fixture
def default_bun():
    """Стандартная булка для тестов"""
    return Bun("Краторная булка N-200i", 1255)

@pytest.fixture
def empty_burger():
    """Пустой бургер для тестов"""
    return Burger()

# Параметризованные фикстуры
@pytest.fixture(params=[
    ("Краторная булка N-200i", 1255),
    ("Флюоресцентная булка R2-D3", 988)
], ids=["krator_bun", "fluorescent_bun"])
def parametrized_bun(request):
    """Булка с разными параметрами"""
    return Bun(*request.param)

@pytest.fixture(params=[
    ("SAUCE", "Соус фирменный Space Sauce", 80),
    ("FILLING", "Биокотлета из марсианской Магнолии", 424)
], ids=["sauce", "filling"])
def parametrized_ingredient(request):
    """Ингредиент с разными параметрами"""
    return Ingredient(*request.param)

# Моки
@pytest.fixture
def mock_bun():
    """Мок-объект булки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Мок булки"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient():
    """Мок-объект ингредиента"""
    ingr = Mock(spec=Ingredient)
    ingr.get_type.return_value = "SAUCE"
    ingr.get_name.return_value = "Мок соуса"
    ingr.get_price.return_value = 50
    return ingr

# Комбинированные фикстуры
@pytest.fixture
def prepared_burger(default_bun):
    """Бургер с предустановленными ингредиентами"""
    burger = Burger()
    burger.set_buns(default_bun)
    burger.add_ingredient(Ingredient("SAUCE", "Соус фирменный Space Sauce", 80))
    burger.add_ingredient(Ingredient("FILLING", "Биокотлета из марсианской Магнолии", 424))
    return burger

@pytest.fixture
def burger_with_mocks(mock_bun, mock_ingredient):
    """Бургер с мок-объектами"""
    burger = Burger()
    burger.set_buns(mock_bun)
    burger.add_ingredient(mock_ingredient)
    return burger

# Фикстуры для Database
@pytest.fixture
def empty_database():
    """Пустая база данных"""
    db = Database()
    db.buns = []
    db.ingredients = []
    return db

@pytest.fixture
def initialized_database():
    """Инициализированная база данных"""
    return Database()