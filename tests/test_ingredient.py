import pytest
from praktikum.ingredient import Ingredient
from data import IngredientData

@pytest.mark.parametrize("ingredient_type, name, price, expected_name, expected_price", [
    (IngredientData.SAUCE_TYPE, IngredientData.SAUCE_NAME, IngredientData.SAUCE_PRICE, IngredientData.SAUCE_NAME,
     IngredientData.SAUCE_PRICE),
    (IngredientData.FILLING_TYPE, IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE,
     IngredientData.FILLING_NAME, IngredientData.FILLING_PRICE),
])
def test_ingredient(ingredient_type, name, price, expected_name, expected_price):
    ingredient = Ingredient(ingredient_type=ingredient_type, name=name, price=price)
    assert ingredient.get_name() == expected_name, f"Название ингредиента должно быть '{expected_name}'."
    assert ingredient.get_price() == expected_price, f"Цена ингредиента должна быть {expected_price}."
    assert ingredient.get_type() == ingredient_type, f"Тип ингредиента должен быть '{ingredient_type}'."
