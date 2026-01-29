import allure
from data import Data, Data_0

class TestIngredients:

    @allure.title('Проверка метода get_price')
    @allure.description('Проверка получения цены соуса')
    def test_get_price_sauce(self, mock_sauce):
        assert mock_sauce.get_price() == Data.sauce_price

    @allure.title('Проверка метода get_price')
    @allure.description('Проверка получения цены начинки')
    def test_get_price_filling(self, mock_filling):
        assert mock_filling.get_price() == Data.filling_price

    @allure.title('Проверка метода get_name')
    @allure.description('Проверка получения названия соуса')
    def test_get_get_name(self, mock_sauce):
        assert mock_sauce.get_name() == Data.sauce_name

    @allure.title('Проверка метода get_name')
    @allure.description('Проверка получения названия начинки')
    def test_get_name(self, mock_filling):
        assert mock_filling.get_name() == Data.filling_name

    @allure.title('Проверка метода get_type')
    @allure.description('Проверка получения типа')
    def test_get_type(self, mock_sauce, mock_filling):
        assert mock_sauce.get_type() == Data.sauce_type
        assert mock_filling.get_type() == Data.filling_type