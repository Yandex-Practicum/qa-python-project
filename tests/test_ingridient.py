import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:
    """Тесты для класса Ingredient"""

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 150.5),
        (INGREDIENT_TYPE_FILLING, "dinosaur", 0),
    ])
    def test_ingredient_init(self, ingredient_type, name, price):
        """Тест инициализации ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.type == ingredient_type
        assert ingredient.name == name
        assert ingredient.price == price

    @pytest.mark.parametrize("ingredient_type, name, price,expected", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, "hot sauce"),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200, "cutlet"),
        (INGREDIENT_TYPE_SAUCE, "chili sauce", 300, "chili sauce"),
    ])
    def test_get_name(self, ingredient_type, name, price, expected):
        """Тест получения названия ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_name()
        assert result == expected

    @pytest.mark.parametrize("ingredient_type, name, price, expected", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, 100),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200.5, 200.5),
        (INGREDIENT_TYPE_SAUCE, "sour cream", 0, 0),
    ])
    def test_get_price(self, ingredient_type, name, price, expected):
        """Тест получения цены ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_price()
        assert result == expected

    @pytest.mark.parametrize("ingredient_type, name, price,expected", [
        (INGREDIENT_TYPE_SAUCE, "hot sauce", 100, INGREDIENT_TYPE_SAUCE),
        (INGREDIENT_TYPE_FILLING, "cutlet", 200, INGREDIENT_TYPE_FILLING),
    ])
    def test_get_type(self, ingredient_type, name, price, expected):
        """Тест получения типа ингредиента"""
        ingredient = Ingredient(ingredient_type, name, price)
        result = ingredient.get_type()
        assert result == expected
        assert result in [INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING]