import pytest
from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

@pytest.fixture
def mock_bun():
    """Фикстура для создания mock-булочки"""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "Краторная булка"
    bun.get_price.return_value = 100
    return bun

@pytest.fixture
def mock_ingredient():
    """Фикстура для создания mock-ингредиента"""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
    ingredient.get_name.return_value = "Сырный соус"
    ingredient.get_price.return_value = 50
    return ingredient

@pytest.fixture
def burger():
    """Фикстура для создания чистого экземпляра Burger"""
    from praktikum.burger import Burger
    return Burger()

@pytest.fixture
def database():
    """Фикстура для создания экземпляра Database"""
    from praktikum.database import Database
    return Database()

@pytest.fixture(params=[
    (INGREDIENT_TYPE_SAUCE, "Сырный соус", 50),
    (INGREDIENT_TYPE_FILLING, "Говяжья котлета", 100)
])
def ingredient_data(request):
    """Фикстура с параметризованными данными для ингредиентов"""
    return request.param