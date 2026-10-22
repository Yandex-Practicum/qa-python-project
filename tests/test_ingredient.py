import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337.0),
        (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 30.0),
        (INGREDIENT_TYPE_FILLING, "Плоды Фалленианского дерева", 874.0)
    ])
    def test_ingredient_get_name(self, ing_type, name, price):
        """Тест: получение названия ингредиента"""
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337.0)
    ])
    def test_ingredient_get_price(self, ing_type, name, price):
        """Тест: получение цены ингредиента"""
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_price() == price

    @pytest.mark.parametrize("ing_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Соус Spicy-X", 90.0),
        (INGREDIENT_TYPE_FILLING, "Мясо бессмертных моллюсков Protostomia", 1337.0)
    ])
    def test_ingredient_get_type(self, ing_type, name, price):
        """Тест: получение типа ингредиента"""
        ingredient = Ingredient(ing_type, name, price)
        assert ingredient.get_type() == ing_type