from data import data
from praktikum.ingredient import Ingredient
import pytest


class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Метеоритный дождь", 20), ("Соус", "Космический ням", 10)],
    )
    def test_create_ingredient_with_name_and_price(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == ingredient_name
        assert ingredient.price == ingredient_price

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Метеоритный дождь", 20), ("Соус", "Космический ням", 10)],
    )
    def test_get_name_ing_success(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Метеоритный дождь", 20), ("Соус", "Космический ням", 10)],
    )
    def test_get_price_ing_success(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price

    @pytest.mark.parametrize(
        "ingredient_data",
        [("начинка", "Метеоритный дождь", 20), ("Соус", "Космический ням", 10)],
    )
    def test_get_type_ing_success(self, ingredient_data):
        ingredient_type, ingredient_name, ingredient_price = ingredient_data
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type
