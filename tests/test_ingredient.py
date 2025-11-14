import pytest
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize("ingredient_type,ingredient_name,ingredient_price", [
    ("соус", "аджика", 50.0),
    ("начинка", "сыыыр", 80.0),
    ("", "жареный лук", 30)
])
def test_ingredient_creation(ingredient_type, ingredient_name, ingredient_price):
    ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == ingredient_name
    assert ingredient.get_price() == ingredient_price

