import allure

from praktikum.bun import Bun

from conftest import mock_db
from data import Data
from praktikum.database import Database
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:

    @allure.title('Тест на получение булочек')
    def test_available_buns(self):
        db = Database()
        assert len(db.buns) == 3

    @allure.title('Тест на получение ингредиентов')
    def test_available_ingredients(self):
        db = Database()
        assert len(db.ingredients) == 6

    @allure.title('Тест на получение булочек (сценарий с использование mock)')
    def test_available_buns_mock(self, mock_db):
        test_buns = [
            Bun(Data.yellow_bun, Data.yellow_bun_price),
            Bun(Data.red_bun, Data.red_bun_price)
        ]
        mock_db.available_buns.return_value = test_buns
        result = mock_db.available_buns()
        assert result == test_buns

    @allure.title('Тест на получение ингредиентов (сценарий с использование mock)')
    def test_available_ingredients_mock(self, mock_db):
        test_ingredients = [
            Ingredient(INGREDIENT_TYPE_FILLING,
                       Data.filling_fish,
                       Data.filling_fish_price),
            Ingredient(INGREDIENT_TYPE_SAUCE,
                       Data.ketchup, Data.ketchup_price),
        ]
        mock_db.available_ingredients.return_value = test_ingredients
        result = mock_db.available_ingredients()
        assert result == test_ingredients
