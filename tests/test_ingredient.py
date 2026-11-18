import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    @pytest.mark.parametrize("ing_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING,
    ])
    def test_get_type(self, ing_type):
        ingredient = Ingredient(ing_type, "Тестовый ингредиент", 100)
        assert ingredient.get_type() == ing_type

    @pytest.mark.parametrize("name", [
        "Соус Spicy-X",
        "Мясо бессмертных моллюсков Protostomia",
        "Сыр",
    ])
    def test_get_name(self, name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("price", [90, 1337, 50])
    def test_get_price(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Тестовый ингредиент", price)
        assert ingredient.get_price() == price