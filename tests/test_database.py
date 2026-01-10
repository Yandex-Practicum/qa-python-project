import allure
from unittest.mock import MagicMock
from Stellar_Burgers.database import Database
from Stellar_Burgers.bun import Bun
from Stellar_Burgers.ingredient import Ingredient

@allure.feature('Проверка класса Database')
class TestDatabase:
    @allure.title('Проверка количества доступных булочек')
    def test_available_buns_count(self):
        mock_bun = MagicMock(spec=Bun)
        db = Database()
        db.buns = [mock_bun, mock_bun, mock_bun]
        assert len(db.available_buns()) == 3

    @allure.title('Проверка имени булочки')
    def test_available_buns_name(self):
        mock_bun = MagicMock(spec=Bun)
        mock_bun.get_name.return_value = "mock bun"
        db = Database()
        db.buns = [mock_bun]
        assert db.available_buns()[0].get_name() == "mock bun"

    @allure.title('Проверка цены булочки')
    def test_available_buns_price(self):
        mock_bun = MagicMock(spec=Bun)
        mock_bun.get_price.return_value = 123
        db = Database()
        db.buns = [mock_bun]
        assert db.available_buns()[0].get_price() == 123

    @allure.title('Проверка количества доступных ингредиентов')
    def test_available_ingredients_count(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        db = Database()
        db.ingredients = [mock_ingredient, mock_ingredient]
        assert len(db.available_ingredients()) == 2

    @allure.title('Проверка имени ингредиента')
    def test_available_ingredients_name(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_name.return_value = "mock ingredient"
        db = Database()
        db.ingredients = [mock_ingredient]
        assert db.available_ingredients()[0].get_name() == "mock ingredient"

    @allure.title('Проверка цены ингредиента')
    def test_available_ingredients_price(self):
        mock_ingredient = MagicMock(spec=Ingredient)
        mock_ingredient.get_price.return_value = 456
        db = Database()
        db.ingredients = [mock_ingredient]
        assert db.available_ingredients()[0].get_price() == 456
