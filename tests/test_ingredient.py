import pytest
from praktikum.ingredient import Ingredient
from data import INGREDIENTS

class TestIngredient:
    @pytest.mark.parametrize(
        "ingredient_data",
        INGREDIENTS,
        ids=[f"{ing['type']}_{ing['name']}" for ing in INGREDIENTS]
    )
    def test_ingredient_initialization(self, ingredient_data):
        """Проверка корректности создания ингредиента"""
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_type() == ingredient_data["type"]
        assert ingredient.get_name() == ingredient_data["name"]
        assert ingredient.get_price() == ingredient_data["price"]

    @pytest.mark.parametrize(
        "ingredient_data",
        INGREDIENTS,
        ids=[ing["name"] for ing in INGREDIENTS]
    )
    def test_get_type(self, ingredient_data):
        """Проверка метода get_type()"""
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_type() == ingredient_data["type"]

    @pytest.mark.parametrize(
        "ingredient_data",
        INGREDIENTS,
        ids=[ing["name"] for ing in INGREDIENTS]
    )
    def test_get_name(self, ingredient_data):
        """Проверка метода get_name()"""
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_name() == ingredient_data["name"]

    @pytest.mark.parametrize(
        "ingredient_data",
        INGREDIENTS,
        ids=[ing["name"] for ing in INGREDIENTS]
    )
    def test_get_price(self, ingredient_data):
        """Проверка метода get_price()"""
        ingredient = Ingredient(
            ingredient_data["type"],
            ingredient_data["name"],
            ingredient_data["price"]
        )
        assert ingredient.get_price() == ingredient_data["price"]