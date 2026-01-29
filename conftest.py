import pytest
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient

@pytest.fixture
def sample_burger():
    # Фикстура для создания экземпляра Burger.
    return Burger()

@pytest.fixture
def sample_bun():
    # Фикстура для создания экземпляра Bun с именем "test bun" и ценой 50.0.
    return Bun("test bun", 50.0)

@pytest.fixture
def sample_ingredient():
    # Фикстура для создания экземпляра Ingredient с типом "test type", именем "test ingredient" и ценой 30.0.
    return Ingredient("test type", "test ingredient", 30.0)

@pytest.fixture
def sample_database():
    # Фикстура для создания экземпляра Database.
    from praktikum.database import Database
    return Database()
