import pytest
from unittest.mock import Mock
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from data.test_data import BunData, IngredientData


@pytest.fixture
def burger():
    from praktikum.burger import Burger
    return Burger()


@pytest.fixture
def bun_mock():
    bun = Mock()
    bun.get_name.return_value = BunData.BLACK_BUN["name"]
    bun.get_price.return_value = BunData.BLACK_BUN["price"]
    return bun


@pytest.fixture
def white_bun_mock():
    bun = Mock()
    bun.get_name.return_value = BunData.WHITE_BUN["name"]
    bun.get_price.return_value = BunData.WHITE_BUN["price"]
    return bun


@pytest.fixture
def red_bun_mock():
    bun = Mock()
    bun.get_name.return_value = BunData.RED_BUN["name"]
    bun.get_price.return_value = BunData.RED_BUN["price"]
    return bun


@pytest.fixture
def black_bun_mock():
    bun = Mock()
    bun.get_name.return_value = BunData.BLACK_BUN["name"]
    bun.get_price.return_value = BunData.BLACK_BUN["price"]
    return bun


@pytest.fixture
def ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.HOT_SAUCE["type"]
    ingredient.get_name.return_value = IngredientData.HOT_SAUCE["name"]
    ingredient.get_price.return_value = IngredientData.HOT_SAUCE["price"]
    return ingredient


@pytest.fixture
def cutlet_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.CUTLET["type"]
    ingredient.get_name.return_value = IngredientData.CUTLET["name"]
    ingredient.get_price.return_value = IngredientData.CUTLET["price"]
    return ingredient


@pytest.fixture
def cheese_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.CHEESE["type"]
    ingredient.get_name.return_value = IngredientData.CHEESE["name"]
    ingredient.get_price.return_value = IngredientData.CHEESE["price"]
    return ingredient


@pytest.fixture
def sour_cream_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.SOUR_CREAM["type"]
    ingredient.get_name.return_value = IngredientData.SOUR_CREAM["name"]
    ingredient.get_price.return_value = IngredientData.SOUR_CREAM["price"]
    return ingredient


@pytest.fixture
def chili_sauce_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.CHILI_SAUCE["type"]
    ingredient.get_name.return_value = IngredientData.CHILI_SAUCE["name"]
    ingredient.get_price.return_value = IngredientData.CHILI_SAUCE["price"]
    return ingredient


@pytest.fixture
def salad_ingredient_mock():
    ingredient = Mock()
    ingredient.get_type.return_value = IngredientData.SALAD["type"]
    ingredient.get_name.return_value = IngredientData.SALAD["name"]
    ingredient.get_price.return_value = IngredientData.SALAD["price"]
    return ingredient


@pytest.fixture
def basic_burger_setup(burger, bun_mock, ingredient_mock, cutlet_ingredient_mock):
    burger.set_buns(bun_mock)
    burger.add_ingredient(ingredient_mock)
    burger.add_ingredient(cutlet_ingredient_mock)
    return burger