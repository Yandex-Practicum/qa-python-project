import pytest
from unittest.mock import Mock
import ingredient_types
from praktikum.burger import Burger
import data


@pytest.fixture
def burger():
    return Burger()

@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = data.NAME_BUN_COSMO
    bun.get_price.return_value = data.PRICE_BUN_INT

    return bun

@pytest.fixture
def mock_burger():
    burger = Mock()
    burger.get_bun.return_value = data.NAME_BUN_COSMO
    burger.get_ingredients.return_value = data.NAME_FILLING_SALAD_MARS

    return Burger()

@pytest.fixture
def mock_ingredients_sauce():
    ingredients = Mock()
    ingredients.get_type.return_value = ingredient_types.INGREDIENT_TYPE_SAUCE
    ingredients.get_name.return_value = data.NAME_ASTROSAUCE
    ingredients.get_price.return_value = data.PRICE_ASTROSAUCE

    return ingredients

@pytest.fixture
def mock_ingredients_filling():
    ingredients = Mock()
    ingredients.get_type.return_value = ingredient_types.INGREDIENT_TYPE_FILLING
    ingredients.get_name.return_value = data.NAME_FILLING_VULKAN_CUTLET
    ingredients.get_price.return_value = data.PRICE_VULKAN_CUTLET

    return ingredients