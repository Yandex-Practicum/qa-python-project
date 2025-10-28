import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from data import (
    SAUCE_NAME, SAUCE_TYPE, SAUCE_PRICE,
    FILLING_NAME, FILLING_TYPE, FILLING_PRICE
)


class TestIngredient:
    """Тестовый класс для ингредиента."""

    @pytest.mark.parametrize("ingredient_type,name,price", [
        (SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE),
        (SAUCE_TYPE, "sour cream", 200.0),
        (FILLING_TYPE, FILLING_NAME, FILLING_PRICE),
        (FILLING_TYPE, "dinosaur", 200.0),
    ])
    def test_ingredient_creation_sets_attributes(self, ingredient_type, name, price):
        """Тест создания ингредиента с установкой атрибутов."""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    def test_get_price_returns_correct_value(self):
        """Тест метода get_price возвращает корректную цену."""
        ingredient = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert ingredient.get_price() == SAUCE_PRICE

    def test_get_name_returns_correct_value(self):
        """Тест метода get_name возвращает корректное имя."""
        ingredient = Ingredient(FILLING_TYPE, FILLING_NAME, FILLING_PRICE)
        assert ingredient.get_name() == FILLING_NAME

    def test_get_type_returns_correct_value(self):
        """Тест метода get_type возвращает корректный тип."""
        ingredient = Ingredient(SAUCE_TYPE, SAUCE_NAME, SAUCE_PRICE)
        assert ingredient.get_type() == SAUCE_TYPE

    @pytest.mark.parametrize("price", [0.0, 0.5, 100.0, 999.99])
    def test_ingredient_with_different_prices(self, price):
        """Тест ингредиентов с разными ценами."""
        ingredient = Ingredient(FILLING_TYPE, "test filling", price)
        assert ingredient.get_price() == price
