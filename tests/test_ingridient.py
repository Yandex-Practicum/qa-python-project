import allure
import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestIngredient:


    @allure.title('Проверка возврата Стоимости')
    @pytest.mark.parametrize(
        "ingredient, name, price", [
            (INGREDIENT_TYPE_SAUCE, 'Bun1', 5.0),
            (INGREDIENT_TYPE_FILLING, 'Bun2', 6.0)
        ]
    )
    def test_get_price(self, ingredient, name, price):
        ingrit = Ingredient(ingredient, name, price)
        result = ingrit.get_price()
        assert result == price


    @allure.title('Проверка возврата Названия')
    @pytest.mark.parametrize(
        "ingredient, name, price", [
            (INGREDIENT_TYPE_SAUCE, 'Bun1', 5.0),
            (INGREDIENT_TYPE_FILLING, 'Bun2', 6.0)
        ]
    )
    def test_get_name(self, ingredient, name, price):
        ingrit = Ingredient(ingredient, name, price)
        result = ingrit.get_name()
        assert result == name


    @allure.title('Проверка возврата ингредиента')
    @pytest.mark.parametrize(
        "ingredient, name, price", [
            (INGREDIENT_TYPE_SAUCE, 'Bun1', 5.0),
            (INGREDIENT_TYPE_FILLING, 'Bun2', 6.0)
        ]
    )
    def test_get_type(self, ingredient, name, price):
        ingrit = Ingredient(ingredient, name, price)
        result = ingrit.get_type()
        assert result == ingredient




