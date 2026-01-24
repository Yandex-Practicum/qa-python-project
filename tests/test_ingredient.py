# tests/test_ingredient.py
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE

@pytest.mark.parametrize("ingredient_type, name, price", [
    (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
    (INGREDIENT_TYPE_FILLING, "cutlet", 150),
    (INGREDIENT_TYPE_SAUCE, "barbecue sauce", 120),
    (INGREDIENT_TYPE_FILLING, "cheese", 80),
])  # Параметризация для проверки нескольких ингредиентов
def test_ingredient_creation(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price
    assert ingredient.get_type() == ingredient_type