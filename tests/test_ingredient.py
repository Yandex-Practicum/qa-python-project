import pytest
import allure
from unittest.mock import Mock
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:


    @allure.title("Проверка получения названия ингредиента")
    @pytest.mark.parametrize("test_name", [
        "Tomato",
        "Cheese",
        "Special Sauce"
    ])
    def test_get_name(self, test_name):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, test_name, 50.0)
        assert ingredient.get_name() == test_name


    @allure.title("Проверка получения цены ингредиента")
    @pytest.mark.parametrize("test_price", [
        100.0,
        250.5,
        0.0
    ])
    def test_get_price(self, test_price):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Test Ingredient", test_price)
        assert ingredient.get_price() == test_price


    @allure.title("Проверка получения типа ингредиента")
    @pytest.mark.parametrize("test_type", [
        INGREDIENT_TYPE_SAUCE,
        INGREDIENT_TYPE_FILLING
    ])
    def test_get_type(self, test_type):
        ingredient = Ingredient(test_type, "Test Ingredient", 100.0)
        assert ingredient.get_type() == test_type


    @allure.title("Проверка с использованием мока для метода get_price")
    def test_mock_get_price(self):
        mock_ingredient = Mock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 150.25
        assert mock_ingredient.get_price() == 150.25


    @allure.title("Проверка создания ингредиента с разными типами, названиями и ценами")
    @pytest.mark.parametrize("ingredient_type,name,price", [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 100.0),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 200.5),
        (INGREDIENT_TYPE_SAUCE, "Chili Sauce", 300.75),
        ("", "Unknown", 0.0)
    ])
    def test_ingredient_initialization(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert (
            ingredient.type == ingredient_type and
            ingredient.name == name and
            ingredient.price == price
    )