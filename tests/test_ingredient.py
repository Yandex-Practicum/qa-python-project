import pytest
import allure
from Stellar_Burgers.ingredient import Ingredient

@allure.feature('Проверка создания ингредиента')
class TestIngredient:
    @allure.title('Проверка типа ингредиента: {ingredient_type}')
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "beef", 100),
        ("SAUCE", "mayo", 40),
    ])
    def test_ingredient_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Тип ингредиента должен быть {ingredient_type}"

    @allure.title('Проверка имени ингредиента: {name}')
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "beef", 100),
        ("SAUCE", "mayo", 40),
    ])
    def test_ingredient_name(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, f"Имя ингредиента должно быть {name}"

    @allure.title('Проверка цены ингредиента: {price}')
    @pytest.mark.parametrize("ingredient_type, name, price", [
        ("SAUCE", "ketchup", 50),
        ("FILLING", "beef", 100),
        ("SAUCE", "mayo", 40),
    ])
    def test_ingredient_price(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, f"Цена ингредиента должна быть {price}"

