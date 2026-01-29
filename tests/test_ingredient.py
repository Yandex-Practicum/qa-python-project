import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.test_data import INGREDIENTS_TEST_DATA

@pytest.mark.parametrize("ingredient_type, name, price", INGREDIENTS_TEST_DATA)
def test_ingredient_properties(ingredient_type, name, price):
    """Тестируем свойства ингредиентов"""
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price

def test_ingredient_get_price():
    """Тестируем метод get_price"""
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.get_price() == 100

def test_ingredient_get_name():
    """Тестируем метод get_name"""
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.get_name() == "hot sauce"

def test_ingredient_get_type():
    """Тестируем метод get_type"""
    ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "hot sauce", 100)
    assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE


