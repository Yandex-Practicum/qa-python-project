import pytest
from unittest.mock import Mock
from praktikum.types import IngredientType


@pytest.fixture
def sample_bun():
    bun = Mock()
    bun.get_name.return_value = "Тестовая булка"
    bun.get_price.return_value = 100.0
    return bun


@pytest.fixture
def sample_sauce():
    sauce = Mock()
    sauce.get_type.return_value = IngredientType.SAUCE
    sauce.get_name.return_value = "Тестовый соус"
    sauce.get_price.return_value = 50.0
    return sauce


@pytest.fixture
def sample_filling():
    filling = Mock()
    filling.get_type.return_value = IngredientType.FILLING
    filling.get_name.return_value = "Тестовая начинка"
    filling.get_price.return_value = 200.0
    return filling
