import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredient:

    @pytest.mark.parametrize("ing_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "Соус традиционный галактический", 15),
        (INGREDIENT_TYPE_FILLING, "Говяжий метеорит", 3000),
        (INGREDIENT_TYPE_SAUCE, "Сыр с астероидной плесенью", 250),
    ])
    def test_ingredient_methods(self, ing_type, name, price):
        """Тестируем только через публичные методы класса"""
        ingredient = Ingredient(ing_type, name, price)

        # Только публичные методы, без прямого доступа к атрибутам
        assert ingredient.get_type() == ing_type
        assert ingredient.get_name() == name
        assert ingredient.get_price() == price