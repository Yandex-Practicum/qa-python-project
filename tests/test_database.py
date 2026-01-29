import allure
import pytest

import data
from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING




class TestDatabase:
    @allure.title('проверка булочек в спинске bans')
    def test_available_buns(self):
        shop = Database()
        buns = shop.available_buns()
        assert len(buns) == 3
        assert buns[0].name == "black bun"
        assert buns[1].name == "white bun"
        assert buns[2].name == "red bun"

    @allure.title('проверка что в конструкторе добавляется 6 единиц ингредиентов')
    def test_available_ingredients(self):
        shop = Database()
        ingredient = shop.available_ingredients()
        assert len(ingredient) == 6

    @allure.title('проверка возвращаемого типа')
    def test_ingredient_types(self):
        shop = Database()
        ingredients = shop.available_ingredients()
        for ingredient in ingredients:
            assert ingredient.type in (INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING)

    @allure.title('проверка содержания всех ожидаемых ингредиентов')
    @pytest.mark.parametrize("expected_ingredient", data.INGREDIENT_DATABASE)
    def test_available_ingredients_all_ing(self, expected_ingredient):
        shop = Database()
        ingredients = shop.available_ingredients()
        type_ing, name, price = expected_ingredient
        assert len(ingredients) == 6
        assert any(ing.type == type_ing and ing.name == name and ing.price == price for ing in ingredients)
