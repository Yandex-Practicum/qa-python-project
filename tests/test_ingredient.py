import allure
import pytest

from praktikum.ingredient import Ingredient

from data import test_ingredient_parametrize_data


@pytest.mark.parametrize(
    "type_of_ingredient, name, price",
    test_ingredient_parametrize_data,
)
class TestIngredient:
    @allure.title("Получение типа ингредиента")
    def test_get_type_ingredient(self, type_of_ingredient, name, price):
        ingredient = Ingredient(type_of_ingredient, name, price)
        assert ingredient.get_type() == type_of_ingredient

    @allure.title("Получение наименования ингредиента")
    def test_get_name_ingredient(self, type_of_ingredient, name, price):
        ingredient = Ingredient(type_of_ingredient, name, price)
        assert ingredient.get_name() == name

    @allure.title("Получение цены ингредиента")
    def test_get_price_ingredient(self, type_of_ingredient, name, price):
        ingredient = Ingredient(type_of_ingredient, name, price)
        assert ingredient.get_price() == price