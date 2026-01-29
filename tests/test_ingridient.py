import allure
from data import Data

class TestIngridientSauce:

    @allure.title('Проверка получения имени соуса через метод get_name')
    def test_get_name_sauce(self, mock_sauce):
        assert mock_sauce.get_name() == Data.Sauce_name

    @allure.title('Проверка получения стоимости соуса через метод get_price')
    def test_get_price_sauce(self, mock_sauce):
        assert mock_sauce.get_price() == Data.Sauce_price

    @allure.title('Проверка получения подтверждения типа данных соуса "str" через метод get_type')
    def test_get_type_sauce(self, mock_sauce):
        assert mock_sauce.get_type() == Data.Sauce_type


class TestIngridientFilling:
    @allure.title('Проверка получения имени начинки через метод get_name')
    def test_get_name_filling(self, mock_filling):
        assert mock_filling.get_name() == Data.Filling_name

    @allure.title('Проверка получения стоимости начинки через метод get_price')
    def test_get_price_filling(self, mock_filling):
        assert mock_filling.get_price() == Data.Filling_price

    @allure.title('Проверка получения подтверждения типа данных начинки "str" через метод get_type')
    def test_get_type_filling(self, mock_filling):
        assert mock_filling.get_type() == Data.Filling_type

