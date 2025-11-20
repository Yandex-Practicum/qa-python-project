import allure
import pytest

import data
from praktikum import ingredient_types
from praktikum.ingredient import Ingredient


class TestIngredient:
    @allure.title('Проверка получения цены ингредиента')
    @pytest.mark.parametrize('ingredient', data.ingredients)
    def test_get_price_ingredients_expected_prices(self, ingredient):
        ingredient_price = ingredient[2]
        ingredient = Ingredient(ingredient[0], ingredient[1], ingredient[2])
        assert ingredient.get_price() == ingredient_price

    @allure.title('Проверка получения названия ингредиента')
    @pytest.mark.parametrize('ingredient', data.ingredients)
    def test_get_name_ingredients_expected_names(self, ingredient):
        ingredient_name = ingredient[1]
        ingredient = Ingredient(ingredient[0], ingredient[1], ingredient[2])
        assert ingredient.get_name() == ingredient_name

    @allure.title('Проверка получения типа ингредиента')
    @pytest.mark.parametrize('ingredient_type', {
        ingredient_types.INGREDIENT_TYPE_FILLING,
        ingredient_types.INGREDIENT_TYPE_SAUCE
    }
                             )
    def test_get_price_ingredients_expected_price(self, ingredient_type):
        ingredient = Ingredient(ingredient_type, data.ingredients[0][1], data.ingredients[0][2])
        assert ingredient.get_type() == ingredient_type

