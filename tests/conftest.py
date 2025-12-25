import pytest
from unittest.mock import Mock
from praktikum.burger import Burger
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


@pytest.fixture
def sample_bun():
    """Фикстура для создания тестовой булочки."""
    return Bun("test bun", 100)


@pytest.fixture
def sample_ingredient():
    """Фикстура для создания тестового ингредиента."""
    return Ingredient(INGREDIENT_TYPE_SAUCE, "test sauce", 50)


@pytest.fixture
def burger():
    """Фикстура для создания бургера."""
    return Burger()


@pytest.fixture
def mock_bun():
    """Фикстура для создания мока булочки."""
    mock = Mock(spec=Bun)
    mock.get_name.return_value = "test bun"
    mock.get_price.return_value = 100
    return mock


@pytest.fixture
def mock_ingredient():
    """Фикстура для создания мока ингредиента."""
    mock = Mock(spec=Ingredient)
    mock.get_name.return_value = "test ingredient"
    mock.get_price.return_value = 50
    mock.get_type.return_value = INGREDIENT_TYPE_SAUCE
    return mock