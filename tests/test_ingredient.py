from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
import pytest


class TestIngredient:

    # Проверка цены ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, 'Соус Spicy-X', 90),
        (INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337),
    ])
    def test_get_price_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

    # Проверка названия ингредиента
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337),
    ])
    def test_get_name_ingredient(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    # Проверка типа ингридиента
    @pytest.mark.parametrize('ingredient_type, name, price, expected_result_ingredient', [
            (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90, "SAUCE"),
            (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337, "FILLING")
        ]
    )
    def test_get_type_ingredient(self, ingredient_type, name, price, expected_result_ingredient):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_result_ingredient
