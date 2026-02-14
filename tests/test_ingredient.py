import pytest
from praktikum.ingredient import Ingredient
from tests.test_constants import (
    TEST_INGREDIENTS, INGREDIENT_TYPE_SAUCE, INGREDIENT_TEST_SAUCE, PRICE_150
)


# Тесты для класса Ingredient.
class TestIngredient:

    @pytest.mark.parametrize("ingredient_type,name,price", TEST_INGREDIENTS)
    def test_ingredient_get_name(self, ingredient_type, name, price):
        # Проверка получения названия ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ingredient_type,name,price", TEST_INGREDIENTS)
    def test_ingredient_get_price(self, ingredient_type, name, price):
        # Проверка получения цены ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ingredient_type,name,price", TEST_INGREDIENTS)
    def test_ingredient_get_type(self, ingredient_type, name, price):
        # Проверка получения типа ингредиента.
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    def test_ingredient_initialization(self):
        # Проверка инициализации ингредиента.
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, INGREDIENT_TEST_SAUCE, PRICE_150)
        assert ingredient.type == INGREDIENT_TYPE_SAUCE
        assert ingredient.name == INGREDIENT_TEST_SAUCE
        assert ingredient.price == PRICE_150
