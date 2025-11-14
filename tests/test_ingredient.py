import pytest
import allure
from prakticum.ingredient import Ingredient
from prakticum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestIngredient:

    @allure.title("Инициализация ингредиента с различными параметрами")
    @pytest.mark.parametrize("ingredient_type,name,price,expected_type,expected_name,expected_price", [
        (INGREDIENT_TYPE_FILLING, "Sausage", 10.5, INGREDIENT_TYPE_FILLING, "Sausage", 10.5),
        (INGREDIENT_TYPE_SAUCE, "Mustard", 2.0, INGREDIENT_TYPE_SAUCE, "Mustard", 2.0),
        (INGREDIENT_TYPE_FILLING, "", 0.0, INGREDIENT_TYPE_FILLING, "", 0.0),  # Пустое имя
        (INGREDIENT_TYPE_SAUCE, "Ketchup", -1.0, INGREDIENT_TYPE_SAUCE, "Ketchup", -1.0),  # Отрицательная цена
    ])

    def test_ingredient_initialization(self, ingredient_type, name, price, expected_type, expected_name,
                                       expected_price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == expected_type
        assert ingredient.get_name() == expected_name
        assert ingredient.get_price() == expected_price

    @allure.title("Проверка метода get_type для разных типов")
    @pytest.mark.parametrize("ingredient_type", [
        INGREDIENT_TYPE_FILLING,
        INGREDIENT_TYPE_SAUCE,
    ])
    def test_get_type_returns_correct_type(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Test", 1.0)
        assert ingredient.get_type() == ingredient_type
        assert isinstance(ingredient.get_type(), str)

    @allure.title("Проверка метода get_name возвращает корректное имя")
    def test_get_name_returns_correct_value(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Tomato", 5.0)
        assert ingredient.get_name() == "Tomato"
        assert isinstance(ingredient.get_name(), str)

    @allure.title("Проверка метода get_price с разными значениями")
    @pytest.mark.parametrize("price", [
        2.0,
        0.0,
        -1.0,
    ])
    def test_get_price_returns_correct_value(self, price):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Mustard", price)
        assert ingredient.get_price() == price
        assert isinstance(ingredient.get_price(), float)

    @allure.title("Тест пустых значений имени и цены")
    def test_empty_name_and_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "", 0.0)
        assert ingredient.get_name() == ""
        assert ingredient.get_price() == 0.0

    @allure.title("Тест невалидной цены (NaN)")
    def test_invalid_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Mystery Ingredient", float('nan'))
        assert ingredient.get_price() != ingredient.get_price()

    @allure.title("Создание нескольких ингредиентов с разными параметрами")
    def test_multiple_ingredients(self):
        ingredient1 = Ingredient(INGREDIENT_TYPE_SAUCE, "Mustard", 2.0)
        ingredient2 = Ingredient(INGREDIENT_TYPE_FILLING, "Cheese", 3.0)
        ingredient3 = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 1.5)

        assert ingredient1.get_name() == "Mustard"
        assert ingredient2.get_name() == "Cheese"
        assert ingredient3.get_name() == "Ketchup"
        assert ingredient1.get_price() == 2.0
        assert ingredient2.get_price() == 3.0
        assert ingredient3.get_price() == 1.5

    @allure.title("Тест обработки отрицательной цены")
    def test_negative_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Expired Sauce", -5.0)
        assert ingredient.get_price() == -5.0

