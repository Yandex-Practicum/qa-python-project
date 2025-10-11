import allure
import pytest

from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE as SAUCE
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING as FILLING
import random


class TestIngredient:
    @allure.title('Проверка типа ингредиентов')
    @pytest.mark.parametrize("ingredient_type", [SAUCE, FILLING])
    def test_get_type_ingredient(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, "Булка", 10.00)
        assert ingredient.get_type() == ingredient_type

    @allure.title('Проверка названия ингредиента')
    def test_get_name_ingredient(self):
        ingredient = Ingredient(random.choice([SAUCE, FILLING]), "Булка", 10.00)
        assert ingredient.get_name() == "Булка"

    @allure.title('Проверка цены ингредиента')
    def test_get_price_ingredient(self):
        ingredient = Ingredient(random.choice([SAUCE, FILLING]), "Булка", 10.00)
        assert ingredient.get_price() == 10.00
