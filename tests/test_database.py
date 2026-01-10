import allure

from data import Data
from conftest import mock_bun, mock_ingredient, db


class TestDatabase:

    @allure.title('Проверяем метод available_buns')
    def test_available_buns_mock_buns_success(self, db, mock_bun):
        mock_bun.get_name.return_value = Data.MOCK_BUN_NAME
        mock_bun.get_price.return_value = Data.MOCK_BUN_PRICE
        mock_buns = [mock_bun]
        db.buns = []
        db.buns.append(mock_buns)
        assert db.available_buns() == db.buns
        assert len(db.buns) == 1

    @allure.title('Проверяем метод available_ingredients')
    def test_available_ingredients_mock_ingredients_success(self, db, mock_ingredient):
        mock_ingredient.get_type.return_value = Data.MOCK_INGREDIENT_TYPE
        mock_ingredient.get_name.return_value = Data.MOCK_INGREDIENT_NAME
        mock_ingredient.get_price.return_value = Data.MOCK_INGREDIENT_PRICE
        mock_ingredients = [mock_ingredient]
        db.ingredients = []
        db.ingredients.append(mock_ingredients)
        assert db.available_ingredients() == db.ingredients
        assert len(db.ingredients) == 1
