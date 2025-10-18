import pytest
from praktikum.ingredient import Ingredient
from praktikum.types import *


class TestIngredient:

    def test_get_price_returns_correct_price(self):
        ingredient = Ingredient(IngredientType.SAUCE, "Соус традиционный галактический", 15.0)
        assert ingredient.get_price() == 15.0

    def test_get_name_returns_correct_name(self):
        ingredient = Ingredient(IngredientType.FILLING, "Говяжий метеорит", 300.0)
        assert ingredient.get_name() == "Говяжий метеорит"

    def test_get_type_returns_correct_type(self):
        ingredient = Ingredient(IngredientType.SAUCE, "Сырный соус", 25.0)
        assert ingredient.get_type() == IngredientType.SAUCE

    def test_filling_type_ingredient(self):
        ingredient = Ingredient(IngredientType.FILLING, "Филе Люминесцентного тетраодонтимформа", 988.0)
        assert ingredient.get_type() == IngredientType.FILLING
        assert ingredient.get_name() == "Филе Люминесцентного тетраодонтимформа"

    def test_ingredient_with_minimal_price(self):
        ingredient = Ingredient(IngredientType.SAUCE, "Минимальный соус", 0.01)
        assert ingredient.get_price() == 0.01
