import pytest
import pytest_check

from database import Database
from ingredient import Ingredient


@pytest.mark.parametrize("ingredient", Database().available_ingredients())
class TestIngredient:
    def test_bun_creation(self, ingredient):
        new_ingredient = Ingredient(ingredient_type=ingredient.type, name=ingredient.name, price=ingredient.price)
        pytest_check.is_true(new_ingredient.type == ingredient.type)
        pytest_check.is_true(new_ingredient.name == ingredient.name)
        assert new_ingredient.price == ingredient.price

    def test_get_type(self, ingredient):
        new_ingredient = Ingredient(ingredient_type=ingredient.type, name=ingredient.name, price=ingredient.price)
        assert new_ingredient.get_type() == ingredient.type

    def test_get_name(self, ingredient):
        new_ingredient = Ingredient(ingredient_type=ingredient.type, name=ingredient.name, price=ingredient.price)
        assert new_ingredient.get_name() == ingredient.name

    def test_get_price(self, ingredient):
        new_ingredient = Ingredient(ingredient_type=ingredient.type, name=ingredient.name, price=ingredient.price)
        assert new_ingredient.get_price() == ingredient.price
