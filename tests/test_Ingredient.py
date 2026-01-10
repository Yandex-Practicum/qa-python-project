import allure
from conftest import *

class TestIngredient:

    @allure.title('Проверка метода get_price для соуса')
    def test_get_price_sauce_works_correctly(self, mock_sauce_two):
        assert mock_sauce_two.get_price() == DataTwo.SAUCE_PRICE

    @allure.title('Проверка метода get_price для начинки')
    def test_get_price_filling_works_correctly(self, mock_filling_two):
        assert mock_filling_two.get_price() == DataTwo.FILLING_PRICE

    @allure.title('Проверка метода get_name для соуса')
    def test_get_name_sauce_works_correctly(self, mock_sauce_one):
        assert mock_sauce_one.get_name() == DataOne.SAUCE_NAME

    @allure.title('Проверка метода get_name для начинки')
    def test_get_name_filling_works_correctly(self, mock_filling_one):
        assert mock_filling_one.get_name() == DataOne.FILLING_NAME

    @allure.title('Проверка метода get_type для соуса')
    def test_get_type_sauce_works_correctly(self, mock_sauce_one):
        assert mock_sauce_one.get_type() == DataOne.SAUCE_TYPE

    @allure.title('Проверка метода get_type для начинки')
    def test_get_type(self, mock_filling_one):
        assert mock_filling_one.get_type() == DataOne.FILLING_TYPE


