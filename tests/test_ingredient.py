# test_ingredient.py

import pytest
from ingredient import Ingredient
from ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestIngredientCoreBehavior:
    """Проверка базового функционирования класса Ingredient"""

    def test_type_storage(self):
        """Проверка, что тип ингредиента корректно сохраняется и возвращается"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", 100)
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE

    def test_name_storage(self):
        """Проверка, что название ингредиента корректно сохраняется и возвращается"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", 150)
        assert ingredient.get_name() == "Котлета"

    def test_price_storage(self):
        """Проверка, что цена ингредиента корректно сохраняется и возвращается"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Соус", 200)
        assert ingredient.get_price() == 200


class TestIngredientDataHandling:
    """Проверка обработки различных вариантов данных"""

    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, "Острый соус", 100),
        (INGREDIENT_TYPE_FILLING, "Котлета", 150),
        ("SPECIAL", "Эксклюзив", 200)
    ])
    def test_various_types_handling(self, ingredient_type, name, price):
        """Проверка, что класс корректно обрабатывает разные типы ингредиентов"""
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    @pytest.mark.parametrize("name", ["Соус", "Очень длинное название ингредиента"])
    def test_various_names_handling(self, name):
        """Проверка, что класс корректно обрабатывает разные варианты названий"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, name, 100)
        assert ingredient.get_name() == name


class TestIngredientEdgeCases:
    """Проверка обработки нестандартных ситуаций"""

    def test_empty_name_handling(self):
        """Проверка, что класс не ломается при передаче пустого названия"""
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 100)
        assert ingredient.get_name() == ""

    def test_negative_price_handling(self):
        """Проверка, что класс не ломается при передаче отрицательной цены"""
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Котлета", -50)
        assert ingredient.get_price() == -50

    def test_unknown_type_handling(self):
        """Проверка, что класс не ломается при передаче нестандартного типа"""
        ingredient = Ingredient("UNKNOWN", "Секретный", 300)
        assert ingredient.get_type() == "UNKNOWN"


class TestIngredientMockUsage:
    """Проверка работы с mock-объектами"""

    def test_mock_type_handling(self, mock_ingredient):
        """Проверка, что mock-объект возвращает заданный тип"""
        assert mock_ingredient.get_type() == "SAUCE"

    def test_mock_name_handling(self, mock_ingredient):
        """Проверка, что mock-объект возвращает заданное название"""
        assert mock_ingredient.get_name() == "Мок соуса"

    def test_mock_price_handling(self, mock_ingredient):
        """Проверка, что mock-объект возвращает заданную цену"""
        assert mock_ingredient.get_price() == 50