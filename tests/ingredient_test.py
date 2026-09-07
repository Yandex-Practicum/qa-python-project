import pytest
from praktikum.ingredient import Ingredient


class TestIngredient:
    """Тесты для класса Ingredient"""

    def test_create_ingredient_with_valid_data(self):
        """Тест создания ингредиента с валидными данными"""
        ingredient = Ingredient("SAUCE", "Ketchup", 1.5)

        assert ingredient.get_name() == "Ketchup"
        assert ingredient.get_price() == 1.5
        assert ingredient.get_type() == "SAUCE"

    def test_create_filling_ingredient(self):
        """Тест создания ингредиента типа начинка"""
        ingredient = Ingredient("FILLING", "Beef Patty", 3.0)

        assert ingredient.get_name() == "Beef Patty"
        assert ingredient.get_price() == 3.0
        assert ingredient.get_type() == "FILLING"

    def test_create_sauce_ingredient(self):
        """Тест создания ингредиента типа соус"""
        ingredient = Ingredient("SAUCE", "Mayonnaise", 1.0)

        assert ingredient.get_name() == "Mayonnaise"
        assert ingredient.get_price() == 1.0
        assert ingredient.get_type() == "SAUCE"

    def test_get_name_returns_correct_name(self):
        """Тест проверки метода get_name"""
        ingredient = Ingredient("FILLING", "Cheese", 2.0)
        assert ingredient.get_name() == "Cheese"

    def test_get_price_returns_correct_price(self):
        """Тест проверки метода get_price"""
        ingredient = Ingredient("SAUCE", "BBQ Sauce", 1.75)
        assert ingredient.get_price() == 1.75

    def test_get_type_returns_correct_type(self):
        """Тест проверки метода get_type"""
        ingredient = Ingredient("FILLING", "Chicken", 2.5)
        assert ingredient.get_type() == "FILLING"

    def test_ingredient_with_zero_price(self):
        """Тест создания ингредиента с нулевой ценой"""
        ingredient = Ingredient("SAUCE", "Free Sauce", 0.0)

        assert ingredient.get_name() == "Free Sauce"
        assert ingredient.get_price() == 0.0
        assert ingredient.get_type() == "SAUCE"

    def test_ingredient_with_empty_name(self):
        """Тест создания ингредиента с пустым названием"""
        ingredient = Ingredient("FILLING", "", 1.0)

        assert ingredient.get_name() == ""
        assert ingredient.get_price() == 1.0
        assert ingredient.get_type() == "FILLING"

    def test_ingredient_with_special_characters_in_name(self):
        """Тест создания ингредиента со специальными символами в названии"""
        ingredient = Ingredient("FILLING", "Patty #1 (XL)", 4.99)

        assert ingredient.get_name() == "Patty #1 (XL)"
        assert ingredient.get_price() == 4.99
        assert ingredient.get_type() == "FILLING"

    def test_ingredient_with_cyrillic_name(self):
        """Тест создания ингредиента с кириллическим названием"""
        ingredient = Ingredient("FILLING", "Говядина", 3.5)

        assert ingredient.get_name() == "Говядина"
        assert ingredient.get_price() == 3.5
        assert ingredient.get_type() == "FILLING"