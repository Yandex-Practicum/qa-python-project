import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from data import Data

@pytest.fixture
def mock_bun():
    """Мок для Bun: имитирует булочку с фиксированным именем и ценой."""
    bun = Mock()
    bun.get_name.return_value = Data.buns[0]
    bun.get_price.return_value = Data.buns[1]
    return bun

@pytest.fixture
def mock_ingredient_factory():
    """Фабрика мока для Ingredient: создает мок с заданным типом, именем, ценой."""
    def create_ingredient(ingredient_type: str, name: str, price: float):
        ingredient = Mock()
        ingredient.get_type.return_value = ingredient_type
        ingredient.get_name.return_value = name
        ingredient.get_price.return_value = price
        return ingredient
    return create_ingredient

@pytest.fixture
def burger(mock_bun):
    """Фикстура Burger: создает burger и устанавливает мок bun."""
    burger = Burger()
    burger.set_buns(mock_bun)
    return burger