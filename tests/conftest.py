import pytest

from unittest.mock import Mock
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient


@pytest.fixture
def mock_bun():
    """Мок для класса Bun."""
    bun = Mock(spec=Bun)
    bun.get_name.return_value = "mock bun"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def mock_ingredient():
    """Мок для класса Ingredient."""
    ingredient = Mock(spec=Ingredient)
    ingredient.get_name.return_value = "mock ingredient"
    ingredient.get_price.return_value = 50.0
    ingredient.get_type.return_value = "SAUCE"
    return ingredient


@pytest.fixture
def mock_burger(mock_bun):
    """Мок для класса Burger с установленной булочкой."""
    burger = Mock()
    burger.bun = mock_bun
    burger.ingredients = []
    return burger
