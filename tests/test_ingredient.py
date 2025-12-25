import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


@pytest.mark.parametrize('ingredient_type, name, price', [ # параметризация класса, без использования фикстуры
    (INGREDIENT_TYPE_SAUCE, "cheese", 39.5),
    (INGREDIENT_TYPE_SAUCE, "salsa", 49.5),
    (INGREDIENT_TYPE_FILLING, "bacon", 79.5),
])
class TestIngredient:
    def test_get_name_ingredient_with_valid_name_returns_expected_name(self, ingredient_type, name, price): # тестирует get_name: возвращает имя заданное при создании объекта
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_name() == name, f"Ожидаемое имя ингредиента: '{name}', но получено: {ingredient.get_name()}"

    def test_get_price_ingredient_with_valid_price_returns_expected_price(self, ingredient_type, name, price):  # тестирует get_price: возвращает цену заданную при создании объекта
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_price() == price, f"Ожидаемая цена ингредиента: {price}, но получено: {ingredient.get_price()}"

    def test_get_type_with_valid_type_returns_expected_type(self, ingredient_type, name, price):  # тестирует get_type: возвращает тип ингредиента заданный при создании объекта
        ingredient = Ingredient(ingredient_type, name, price)

        assert ingredient.get_type() == ingredient_type, f"Ожидаемый тип ингредиента: {ingredient_type}, но получено: {ingredient.get_type()}"