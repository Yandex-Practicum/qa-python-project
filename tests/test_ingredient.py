import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


# Тесты на класс Ingredient
class TestIngredient:
    # Проверка корректного сохранения типа ингредиента
    @pytest.mark.parametrize("type_, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_type(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_type() == type_

    # Проверка корректного сохранения имени ингредиента
    @pytest.mark.parametrize("type_, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_name(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_name() == name

    # Проверка корректного сохранения цены ингредиента
    @pytest.mark.parametrize("type_, name, price",
                             [(INGREDIENT_TYPE_SAUCE, "горячий соус", 100), (INGREDIENT_TYPE_FILLING, "сыр", 70), ], )
    def test_ingredient_price(self, type_, name, price):
        ingredient = Ingredient(type_, name, price)
        assert ingredient.get_price() == price
