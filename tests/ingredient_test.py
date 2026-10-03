import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Chili Sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "Cutlet", 250.50)
        ]
    )
    # 1. Проверяем только тип ингредиента
    def test_ingredient_get_type_returns_correct_value(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Chili Sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "Cutlet", 250.50)
        ]
    )
    # 2. Проверяем только имя ингредиента
    def test_ingredient_get_name_returns_correct_value(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name

    @pytest.mark.parametrize(
        "ingredient_type, name, price",
        [
            (INGREDIENT_TYPE_SAUCE, "Chili Sauce", 100.0),
            (INGREDIENT_TYPE_FILLING, "Cutlet", 250.50),
            (INGREDIENT_TYPE_SAUCE, "Sour cream", 0.0) # Граничное значение
        ]
    )
    # 3. Проверяем только цену ингредиента
    def test_ingredient_get_price_returns_correct_value(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price

