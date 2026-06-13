import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from data import TEST_INGREDIENT_DATA

class TestIngredient:

    @pytest.mark.parametrize("ingredient_type, expected_type", TEST_INGREDIENT_DATA["types"])
    def test_get_type_returns_correct_type(self, ingredient_type, expected_type):
        """Метод get_type возвращает правильный тип."""
        ingredient = Ingredient(ingredient_type, "Название ингридиента", 100.0)
        assert ingredient.get_type() == expected_type

    @pytest.mark.parametrize("name, expected_name", TEST_INGREDIENT_DATA["names"])
    def test_get_name_returns_correct_name(self, name, expected_name):
        """Метод get_name возвращает правильное имя."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100.0)
        assert ingredient.get_name() == expected_name

    @pytest.mark.parametrize("price, expected_price", TEST_INGREDIENT_DATA["prices"])
    def test_get_price_returns_correct_price(self, price, expected_price):
        """Метод get_price возвращает правильную цену."""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Название ингридиента", price)
        assert ingredient.get_price() == expected_price



